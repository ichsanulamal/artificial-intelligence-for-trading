import pandas as pd
import numpy as np
import scipy.stats as stats


def analyze_returns(net_returns):
    """
    Perform a one-tailed t-test with the null hypothesis that the mean return is zero,
    and the alternative that the mean return is greater than zero.

    Parameters
    ----------
    net_returns : Pandas Series
        A Pandas Series for each date

    Returns
    -------
    t_value : float
        t-statistic from t-test
    p_value : float
        Corresponding one-tailed p-value
    """
    null_hypothesis = 0.0

    # Perform two-tailed t-test
    t_stat, p_two_tailed = stats.ttest_1samp(net_returns, popmean=null_hypothesis)

    # Convert to one-tailed p-value (alternative hypothesis: mean > 0)
    if t_stat > 0:
        p_one_tailed = p_two_tailed / 2
    else:
        p_one_tailed = 1 - (p_two_tailed / 2)

    return t_stat, p_one_tailed


def test_run(filename="net_returns.csv"):
    """Test run analyze_returns() with net strategy returns from a file."""
    df = pd.read_csv(filename, header=0, index_col=0)
    net_returns = df.iloc[:, 0]  # Assume the first column contains the returns
    t, p = analyze_returns(net_returns)
    print("t-statistic: {:.3f}\np-value: {:.6f}".format(t, p))


if __name__ == "__main__":
    test_run()
