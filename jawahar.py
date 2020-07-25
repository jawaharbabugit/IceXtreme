df['Day_Perc_Change'] = df['Total Traded Quantity'].pct_change().fillna(0)
    
df.loc[(df['Day_Perc_Change'] > -0.5 )& (df['Day_Perc_Change'] <= 0.5), 'Trend'] = 'Slight or No change' 
    

 
    
    
    
        
df.loc[(df['Day_Perc_Change'] > 0.5 )& (df['Day_Perc_Change'] <= 1), 'Trend'] = 'Slight positive'
df.loc[(df['Day_Perc_Change'] > -1 )& (df['Day_Perc_Change'] <= -0.5), 'Trend'] = 'Slight negative'
df.loc[(df['Day_Perc_Change'] > 1 )& (df['Day_Perc_Change'] <= 3), 'Trend'] = 'Positive' 
df.loc[(df['Day_Perc_Change'] > -3 )& (df['Day_Perc_Change'] <= -1), 'Trend'] = 'Negative' 
df.loc[(df['Day_Perc_Change'] > 3 )& (df['Day_Perc_Change'] <= 7), 'Trend'] = 'Among top gainers' 
df.loc[(df['Day_Perc_Change'] > -7 )& (df['Day_Perc_Change'] <= -3), 'Trend'] = 'Among top losers'
df.loc[(df['Day_Perc_Change'] > 7 ), 'Trend'] = 'Bull run'
df.loc[df['Day_Perc_Change'] <= -7 , 'Trend'] = 'Bear drop'
