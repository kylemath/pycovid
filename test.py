from pycovid import pycovid




# pycovid.plot_countries_trend(countries=['Italy', 'Japan', 'US', 'Germany', 'Portugal', 'Bulgaria', 'Spain', 'Sweden'],
# 			casetype=['confirmed'], cumulative=True, start_date="2020-01-01", plottype="linear")

# pycovid.plot_countries_trend(countries=['Canada'],
# 			casetype=['confirmed'], cumulative=True, start_date="2020-01-01", plottype="linear")


# pycovid.plot_provinces(country=['China'],  
# 			casetype=['confirmed'], start_date="2019-10-01", plottype="linear",
# 			proportion=False, cumulative=True)
# pycovid.plot_provinces(country=['France'],  
# 			casetype=['confirmed'], start_date="2019-12-01", plottype="log",
# 			proportion=False, cumulative=True)
pycovid.plot_USstates(casetype=['confirmed'], start_date="2019-12-01", cumulative=False, plottype='log')

pycovid.plot_provinces(country=['Canada'],  
			casetype=['confirmed'], start_date="2019-12-01", plottype="log",
			cumulative=True)
pycovid.plot_provinces_percapita(country=['Canada'],  
			casetype=['confirmed'], start_date="2019-12-01", plottype="log",
			cumulative=True)

pycovid.plot_countries(metric='log_confirmed')


