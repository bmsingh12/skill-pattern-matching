seq_test = {'CAST SQL Builder': 0.3157894736842105,
            'Data Recovery Software SQL Server Data Recovery': 0.12,
            'MS SQL SERVER': 0.375,
            'Micosoft SQL Server Analysis Services SSAS': 0.13333333333333333,
            'Microsoft Azure SQL Data Warehouse': 0.16216216216216217,
            'Microsoft Azure SQL Database': 0.1935483870967742,
            'Microsoft SQL Server': 0.2608695652173913,
            'Microsoft SQL Server Integration Services SSIS': 0.12244897959183673,
            'Microsoft SQL Server Reporting Services SSRS': 0.1276595744680851,
            'Microsoft transact-structural query language T-SQL': 0.11320754716981132,
            'Mimer SQL': 0.5,
            'NonStop SQL': 0.42857142857142855,
            'Oracle PL/SQL': 0.375,
            'Oracle SQL Developer': 0.2608695652173913,
            'Oracle SQL Loader': 0.3,
            'Oracle SQL Plus': 0.3333333333333333,
            'PL/SQL': 0.6666666666666666,
            'Postgres SQL': 0.4,
            'Quest SQL Optimizer for Oracle': 0.18181818181818182,
            'Redgate SQL Server': 0.2857142857142857,
            'SAP SQL Anywhere': 0.3157894736842105,
            'SQL JS': 0.6666666666666666,
            'SentryOne SQL Sentry': 0.2608695652173913,
            'SoftRisk Technologies SoftRisk SQL': 0.16216216216216217,
            'Spark SQL': 0.5,
            'Structure query language SQL': 0.1935483870967742,
            'Structured query language SQL': 0.1875,
            'T-SQL': 0.75,
            'Windent SQL': 0.42857142857142855}

# seq_test = {}


def check():
    return None if seq_test == {} else print(max(seq_test, key=seq_test.get), ":", max(seq_test.values()))

check()

