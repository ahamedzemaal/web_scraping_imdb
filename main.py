from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Movie List'
sheet.append(['Movie Name', 'Year', 'Rating'])


try:
    response = requests.get("https://www.imdb.com/list/ls055386972/")
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find('div', class_="lister-list").find_all(class_="lister-item-header")
    movies_rate = soup.find('div', class_="lister-list").find_all(class_='ipl-rating-star small')

    # Code for Movie Names and it's Year ****

    for movie in movies:
        # print(movie)
        movie_name = movie.find('a').text
        year = movie.find('span' , class_='lister-item-year text-muted unbold').text
        print(movie_name, year)
        break
    # Code for it's Rating *****

    # for rate in movies_rate:
    #     rates = rate.find('span',class_='ipl-rating-star__rating').text
    #     print(rates)
    #     break

    for movie, rate in zip(movies, movies_rate):
    # Extract movie information
        movie_name = movie.find('a').text
        year = movie.find('span', class_='lister-item-year text-muted unbold').text

    # Extract rating information
        rates = rate.find('span', class_='ipl-rating-star__rating').text

    # Print movie details
        # print(f"{movie_name} ({year}) - Rating: {rates}")
        print(movie_name,year, "-",rates)
        sheet.append([movie_name,year,rates])

except Exception as e:
    print(e)

excel.save("Movies.xlsx")