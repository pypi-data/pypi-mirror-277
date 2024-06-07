import pytest
from ramp.core.core import Appliance
from scipy import stats
import matplotlib.pyplot as plt

# create a dummy appliance, then test coincidence = min(self.number, max(1, math.ceil(random.gauss(mu=(self.number * mu_peak + 0.5), sigma=(s_peak * self.number * mu_peak))))) within self.calc_coincident_switch_on(), related to https://github.com/RAMP-project/RAMP/issues/11

appliance = Appliance(user=None, number=10, fixed="no")

# Generate a sample of 'coincidence' values
sample_size = 1000
coincidence_sample = []
for _ in range(sample_size):
    coincidence = appliance.calc_coincident_switch_on(inside_peak_window=True)
    coincidence_sample.append(coincidence)

# # Perform the Shapiro-Wilk test for normality
# _, p_value = stats.shapiro(coincidence_sample)

plt.plot(coincidence_sample)
plt.show()

# # Assert that the p-value is greater than a chosen significance level
# assert p_value > 0.05, "The 'coincidence' values are not normally distributed."
