.. code:: ipython3

    import numpy as np
    import pandas as pd
    from ramp import Plot
    import matplotlib.pyplot as plt

.. code:: ipython3

    R = np.linspace(1, 2, 50)
    R
    # plt.plot(R, np.log(R), label="log")
    plt.plot(R, 1 / R - np.log(R))
    plt.legend()
    plt.show()


.. parsed-literal::

    No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.



.. image:: output_1_1.png


.. code:: ipython3

    ln(r - R)

.. code:: ipython3

    profiles = []

.. code:: ipython3

    profiles.extend(results.tolist())
    profiles




.. parsed-literal::

    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]



.. code:: ipython3

    daily_profiles = np.zeros((4, 3))
    i = 0

.. code:: ipython3

    daily_profiles[i, :] = results
    i = i + 1
    daily_profiles




.. parsed-literal::

    array([[1., 2., 3.],
           [1., 2., 3.],
           [1., 2., 3.],
           [1., 2., 3.]])



.. code:: ipython3

    profiles = daily_profiles.reshape(1, 12).squeeze()

.. code:: ipython3

    res = {}

.. code:: ipython3

    res["column"] = pd.Series(data=profiles)

.. code:: ipython3

    Plot(pd.concat(res, axis=1))




.. parsed-literal::

       column
    0     1.0
    1     2.0
    2     3.0
    3     1.0
    4     2.0
    5     3.0
    6     1.0
    7     2.0
    8     3.0
    9     1.0
     ......



.. code:: ipython3

    days = pd.date_range(start="2023-01-01", periods=7)
    upsampled = pd.date_range(
        start=days[0], end=days[-1] + pd.Timedelta(1, "d") - pd.Timedelta(1, "T"), freq="T"
    )
    upsampled




.. parsed-literal::

    DatetimeIndex(['2023-01-01 00:00:00', '2023-01-01 00:01:00',
                   '2023-01-01 00:02:00', '2023-01-01 00:03:00',
                   '2023-01-01 00:04:00', '2023-01-01 00:05:00',
                   '2023-01-01 00:06:00', '2023-01-01 00:07:00',
                   '2023-01-01 00:08:00', '2023-01-01 00:09:00',
                   ...
                   '2023-01-07 23:50:00', '2023-01-07 23:51:00',
                   '2023-01-07 23:52:00', '2023-01-07 23:53:00',
                   '2023-01-07 23:54:00', '2023-01-07 23:55:00',
                   '2023-01-07 23:56:00', '2023-01-07 23:57:00',
                   '2023-01-07 23:58:00', '2023-01-07 23:59:00'],
                  dtype='datetime64[ns]', length=10080, freq='T')



.. code:: ipython3

    import datetime
    
    today = datetime.datetime.today()
    today




.. parsed-literal::

    datetime.datetime(2023, 11, 30, 23, 35, 41, 952658)



.. code:: ipython3

    datetime.datetime(today.year, today.month, today.day)




.. parsed-literal::

    datetime.datetime(2023, 11, 30, 0, 0)



.. code:: ipython3

    d = pd.date_range(end=datetime.datetime(2020, 1, 1), periods=1)
    d




.. parsed-literal::

    DatetimeIndex(['2020-01-01'], dtype='datetime64[ns]', freq='D')



.. code:: ipython3

    d[-1] + datetime.timedelta(hours=23, minutes=59)




.. parsed-literal::

    Timestamp('2023-11-30 23:59:00', freq='D')



:download:`Link to the jupyter notebook file </../notebooks/Untitled1.ipynb>`.
