import numpy as np
import pandas as pd

class ReturnsCalc:

    def __init__(self,
                 experience_premium=0.025):
        
        self.experience_premium = experience_premium
        self.experience = pd.DataFrame({'years_of_experience': list(range(52))})
        self.experience.loc[:, 'experience_adjustment'] = (1 + experience_premium)**(self.experience.loc[:, 'years_of_experience'])
    
        self.excel_sheet = pd.ExcelFile('../data/reasonable/excellentstudentsocialr.xlsx')
        self.crime_risk_factor = self.excel_sheet.parse('Meta')[['Age', 'Crime Risk Factor']]

        self.meta_df = self.excel_sheet.parse('Meta')[['Years of Education', 
                                                       ' Pretax Income', 
                                                       'Benefits', 
                                                       'Unemployment Probability', 
                                                       'Completion Probability', 
                                                       'Participation Rate']].head(11)

        exp_norm = [np.mean(self.experience.loc[0:i,'experience_adjustment']) for i in range(self.experience.shape[0]-1, self.experience.shape[0]-12,-1)]
        self.meta_df.loc[:, 'Experience Normalization'] = exp_norm

        self.tuition = self.excel_sheet.parse('Meta').loc[0, ['High School Tuition', 
                                                              'College Tuition', 
                                                              'School Feelings', 
                                                              'Nonparticipation Transfers']]
        self.social_data = self.excel_sheet.parse('Meta').loc[:, ['Social Income', 
                                                                  'Social Benefits', 
                                                                  'Social Unemployment', 
                                                                  'Social Crime Cost',	
                                                                  'Social Participation']]

        self.start_age = self.meta_df.loc[1,'Years of Education']+6
        self.pretax_income = self.meta_df.loc[1, ' Pretax Income']
        self.benefits = self.meta_df.loc[1, 'Benefits']
        self.unemployment_probability = self.meta_df.loc[1, 'Unemployment Probability']
        self.participation = self.meta_df.loc[1, 'Participation Rate']
        self.experience_normalization = self.meta_df.loc[1, 'Experience Normalization']
        self.completion_probability = self.meta_df.loc[1, 'Completion Probability']
        
        self.initial_social_participation = self.meta_df.loc[1, 'Completion Probability']
        self.completion_probability = self.meta_df.loc[1, 'Completion Probability']
        self.initial_social_participation = self.social_data.loc[0, 'Social Participation']
        self.initial_unemployment = self.meta_df.loc[0, 'Unemployment Probability']
        

        self.social_returns = self.compute_social_returns(self.start_age,
                                                          self.pretax_income,
                                                          self.benefits,
                                                          self.unemployment_probability,
                                                          self.participation,
                                                          self.experience_normalization,
                                                          self.completion_probability,
                                                          self.initial_social_participation,
                                                          self.initial_unemployment)

    def compute_social_returns(self,
                               start_age,
                               pretax_income,
                               benefits,
                               unemployment_probability,
                               participation,
                               experience_normalization,
                               completion_probability,
                               initial_social_participation,
                               initial_unemployment):

        res = pd.DataFrame({'Age': list(range(15,91))})
        return res