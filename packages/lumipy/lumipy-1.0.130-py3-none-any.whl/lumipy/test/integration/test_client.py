import time
import json
import os

import pandas as pd
from lumipy import LumiError
from lumipy.query_job import QueryJob
from lumipy.test.test_infra import BaseIntTest
from luminesce import ApiException
from luminesce.models.task_status import TaskStatus
from semver import Version
import asyncio

if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class ClientTests(BaseIntTest):

    def test_get_domain_from_url(self):
        domain = self.client.get_domain()
        self.assertEqual(domain, 'fbn-ci')

    def test_client_synchronous_query(self):
        df = self.client.query_and_fetch(
            'select PortfolioCode, PortfolioScope, PortfolioType, BaseCurrency from lusid.portfolio where portfolioscope = \'Finbourne-Examples\' limit 10'
        )
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (10, 4))

    def test_client_background_query(self):
        sql_str = "select * from Sys.Field limit 100"
        ex_id = self.client.start_query(sql_str)
        self.assertIsInstance(ex_id, str)
        self.assertGreater(len(ex_id), 0)

        status = self.client.get_status(ex_id)['status']
        while not status == TaskStatus.RANTOCOMPLETION:
            status = self.client.get_status(ex_id)['status']
            time.sleep(1)

        df = self.client.get_result(ex_id)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 100)

    def test_client_field_table_catalog(self):
        df = self.client.table_field_catalog()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(df.shape[0], 0)

    def test_client_run_synchronous(self):
        df = self.client.run('select PortfolioCode, PortfolioScope, PortfolioType, BaseCurrency from lusid.portfolio limit 10')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (10, 4))

    def test_client_run_asynchronous(self):
        job = self.client.run('select PortfolioCode, PortfolioScope, PortfolioType, BaseCurrency from lusid.portfolio limit 10', return_job=True)
        self.assertIsInstance(job, QueryJob)

        job.monitor()
        df = job.get_result()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (10, 4))

        log = job.get_progress()
        self.assertIsInstance(log, str)
        self.assertGreater(len(log), 0)

    def test_pandas_read_csv_passdown_get_results(self):
        sql_str = "select ^, 'N/A' as NA_TEST from Sys.Field limit 100"
        ex_id = self.client.start_query(sql_str)
        self.assertIsInstance(ex_id, str)
        self.assertGreater(len(ex_id), 0)

        status = self.client.get_status(ex_id)['status']
        while not status == TaskStatus.RANTOCOMPLETION:
            status = self.client.get_status(ex_id)['status']
            time.sleep(1)

        # Keep N/A
        df = self.client.get_result(ex_id, keep_default_na=False, na_values=['NULL'])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 100)
        self.assertEqual(df[~df.NA_TEST.isna()].shape[0], 100)

        # N/A as nan
        df = self.client.get_result(ex_id)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 100)
        self.assertEqual(df[~df.NA_TEST.isna()].shape[0], 0)

    def test_pretty(self):
        sql_str = "select a, b, c, d, e, f as NA_TEST from Sys.Field limit 10"
        pretty_sql = self.client.pretty(sql_str, uppercase_keywords=True, expand_comma_lists=True)
        self.assertEqual(type(pretty_sql), str)
        self.assertEqual(pretty_sql.count('\n'), 8)

    def test_pandas_read_csv_passdown_query_and_fetch(self):
        sql_str = "select ^, 'N/A' as NA_TEST from Sys.Field limit 100"

        # Keep N/A
        df = self.client.query_and_fetch(sql_str, keep_default_na=False, na_values=['NULL'])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 100)
        self.assertEqual(df[~df.NA_TEST.isna()].shape[0], 100)

        # N/A as nan
        df = self.client.query_and_fetch(sql_str)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 100)
        self.assertEqual(df[~df.NA_TEST.isna()].shape[0], 0)

    def test_pandas_read_csv_passdown_run(self):
        sql_str = "select ^, 'N/A' as NA_TEST from Sys.Field limit 100"

        # Keep N/A
        df = self.client.run(sql_str, keep_default_na=False, na_values=['NULL'])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 100)
        self.assertEqual(df[~df.NA_TEST.isna()].shape[0], 100)

        # N/A as nan
        df = self.client.run(sql_str)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 100)
        self.assertEqual(df[~df.NA_TEST.isna()].shape[0], 0)

    def test_get_result_throws_custom_error_class(self):

        try:
            self.client.run('select * from lusid.logs.requesttrace')
        except LumiError as le:
            self.assertIsNotNone(le.ex_id)
            self.assertEqual('Faulted', le.status)
            self.assertEqual("'You must uniquely filter on RequestId to use Lusid.Logs.RequestTrace.'", le.details)

    # noinspection SqlResolve,SqlNoDataSourceInspection
    def test_get_result_datetimes(self):
        df = self.client.run('''
            SELECT
               [Timestamp]
            FROM
               [Lusid.Logs.AppRequest]
            LIMIT 10
        ''')
        self.assertEqual(df.shape[0], 10)
        self.assertTrue(all(isinstance(t, pd.Timestamp) for t in df.Timestamp))

    def test_python_provider_download_version_does_not_exist(self):
        try:
            self.client.download_binary('Python_Providers', 'not-a-binary')
        except ApiException as ae:
            self.assertEqual(400, ae.status)
            self.assertEqual('File Finbourne.Luminesce.PythonProviders of version not-a-binary does not exist.', ae.reason)

    def test_download_binary_version_not_allowed(self):
        try:
            self.client.download_binary('CommandLineTool', '1.14.1')
        except ApiException as ae:
            self.assertEqual(400, ae.status)
            self.assertEqual('Cannot validate SHAs for Finbourne.Luminesce.Cli.1.14.1: version not allowed.', ae.reason)

    def test_download_binary_version_happy(self):
        ver = self.client.download_binary('Python_Providers')

        ver_parsed = Version.parse(ver)
        self.assertTrue(ver_parsed.major==1)
        self.assertTrue(ver_parsed.minor>=0)

    def test_certs_download(self):
        self.client.download_certs()
