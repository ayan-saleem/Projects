import pandas as pd
from termcolor import colored as cl
from io import StringIO

def test_data_import():
    data = StringIO(
        'V1,V2,V3,Amount,Class\n' +
        '0.098698,0.253938,0.830136,3.67,0\n' +
        '-1.753835,2.035333,-0.283746,10.95,0\n' +
        '-0.925810,0.381942,1.206216,9.81,0\n' +
        '-0.843856,0.697929,-0.020260,10.00,0\n' +
        '1.260522,-0.685902,-0.020151,6.49,0\n' +
        '-0.914573,-1.275645,1.070256,4.49,1\n' +
        '-0.326794,0.485070,-1.486375,21.00,1\n' +
        '-0.660527,1.087554,-0.012037,42.00,1\n' +
        '-2.306156,1.585505,-0.727062,1.00,1\n' +
        '0.329594,0.654821,-0.527347,15.00,0\n'
    )
    df = pd.read_csv(data)
    df.drop('Time', axis=1, inplace=True)
    assert len(df) == 10
    assert len(df.columns) == 4

def test_case_amount_stats():
    data = StringIO(
        'V1,V2,V3,Amount,Class\n' +
        '0.098698,0.253938,0.830136,3.67,0\n' +
        '-0.914573,-1.275645,1.070256,4.49,1\n' +
        '-0.326794,0.485070,-1.486375,21.00,1\n' +
        '1.260522,-0.685902,-0.020151,6.49,0\n' +
        '-0.925810,0.381942,1.206216,9.81,0\n'
    )
    df = pd.read_csv(data)
    df.drop('Time', axis=1, inplace=True)
    nonfraud_cases = df[df.Class == 0]
    fraud_cases = df[df.Class == 1]
    assert nonfraud_cases.Amount.mean() == 6.492
    assert fraud_cases.Amount.mean() == 11.996
    assert nonfraud_cases.Amount.median() == 6.49
    assert fraud_cases.Amount.median() == 9.81

def test_case_count_stats():
    data = StringIO(
        'V1,V2,V3,Amount,Class\n' +
        '0.098698,0.253938,0.830136,3.67,0\n' +
        '-1.753835,2.035333,-0.283746,10.95,0\n' +
        '-0.925810,0.381942,1.206216,9.81,0\n' +
        '-0.843856,0.697929,-0.020260,10.00,0\n' +
        '1.260522,-0.685902,-0.020151,6.49,0\n' +
        '-0.914573,-1.275'
    )



