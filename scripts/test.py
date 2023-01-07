import sys
sys.path.append('..')

from ed_ret.returns import ReturnsCalc

r = ReturnsCalc()
# print(r.experience.head(3))
# print(r.crime_risk_factor.head(3))
# print(r.meta_df.columns.tolist())
# print(r.meta_df.head(3))
print(r.social_returns.head())
