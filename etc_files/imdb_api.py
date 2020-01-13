import imdb
import logging


def getMovieDatabyName(name):
    ia = imdb.IMDb(accessSystem='http', reraiseExceptions=True, loggingLevel="critical")
    try:
        movies = ia.search_movie(name)
    except:
        return False

    if len(movies) == 0:
        return False
    movie = movies[0]

    if movie is None:
        return False

    if movie.get("title") is None:
        return False

    ia.update(movie, info=['plot', 'main', 'synopsis'])


    title = movie.get("title")
    year = movie.get("year")
    genre = movie.get("genre")
    plot = ""
    synopsis = ""
    if movie.get("plot") is not None:
        plot = movie.get("plot")[0]

    if movie.get("synopsis") is not None:
        synopsis = movie.get("synopsis")[0]
    castList = movie.get("cast")
    castStr = ""
    if castList is not None:
        cast = []
        for x in castList:
            cast.append(x['name'])

        castStr = ", ".join(cast)
    cover = ""
    if movie.get("cover url") is not None:
        cover = movie.get("cover url")

    # print("GOT MOVIE DATA FOR "+title)
    return title, year, genre, plot, synopsis, castStr, str(cover)


def getMovieDatabyID(mvid):
    ia = imdb.IMDb(accessSystem='http', reraiseExceptions=True, loggingLevel="critical")
    try:
        logger = logging.getLogger('imdbpy')
        logger.disabled = True
        movie = ia.get_movie(mvid)
    except:
        return False
    title = movie.get("title")
    year = movie.get("year")
    genre = movie.get("genre")
    plot = ""
    synopsis = ""
    if movie.get("plot") is not None:
        plot = movie.get("plot")[0]

    if movie.get("synopsis") is not None:
        synopsis = movie.get("synopsis")[0]
    castList = movie.get("cast")
    castStr = ""
    if castList is not None:
        cast = []
        for x in castList:
            cast.append(x['name'])

        castStr = ", ".join(cast)

    cover = ""
    if movie.get("cover url") is not None:
        cover = movie.get("cover url")

    # print("GOT MOVIE DATA FOR " + title)
    return title, year, genre, plot, synopsis, castStr, str(cover)




# ia = imdb.IMDb(accessSystem='http', reraiseExceptions=True, loggingLevel="critical")
# movies = ia.search_movie("2012 Supernova (2009)")
# print(movies[0])

# x = getMovieDatabyID(mvid='0816692')
# x = getMovieDatabyName("2012 Supernova (2009)")
# if x is not False:
#     print(x[0])
# else:
#     print("False")

# ia = imdb.IMDb(accessSystem='http')
# movie = ia.get_movie('0816692')
# print(movie.get('industry'))