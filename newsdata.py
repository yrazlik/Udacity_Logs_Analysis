#!/usr/bin/env python3
import psycopg2

# What are the most popular three articles of all time?
query_top_articles = """SELECT articles.title, COUNT(*) as viewCount
    FROM articles JOIN log
    ON log.path LIKE concat('%', articles.slug, '%')
    WHERE log.status LIKE '%200%'
    GROUP BY articles.title
    ORDER BY viewCount DESC
    LIMIT 3;"""

# Who are the most popular article authors of all time?
query_top_authors = """SELECT authors.name, COUNT(*) as viewCount
    FROM authors JOIN articles
    ON authors.id = articles.author
    JOIN log
    ON log.path LIKE concat('/article/%', articles.slug)
    GROUP BY authors.name
    ORDER BY viewCount DESC
    LIMIT 3;
    """

# On which days did more than 1% of requests lead to errors?
query_errors = """SELECT total.day,
    ROUND(((errors.error_count * 1.0) / (total.requests * 1.0)), 3) AS percent
    FROM (SELECT date_trunc('day', time) "day", COUNT(*) AS error_count
        FROM log
        WHERE status LIKE '%404%'
        GROUP BY day)
    AS errors
    JOIN (SELECT date_trunc('day', time) "day", COUNT(*) AS requests
        FROM log
        GROUP BY day)
    AS total
    ON total.day = errors.day
    WHERE
    (ROUND(((errors.error_count * 1.0) / (total.requests * 1.0)), 3) > 0.01)
    ORDER BY percent DESC;
    """


# Query the db
def execute_query(query):
    connection = psycopg2.connect(database="news")
    cursor = connection.cursor()
    cursor.execute(query)
    result_rows = cursor.fetchall()
    connection.close()
    return result_rows


# Get the top three articles
def get_top_three_articles():
    top_three_articles = execute_query(query_top_articles)
    print ("\n" + "*** TOP 3 ARTICLES ***")

    order = 1
    for title, viewCount in top_three_articles:
        print(str(order) + ". " + "\"" + title + "\"" +
              " -- " + str(viewCount) + " views.")
        order += 1


# Get the top authors
def get_top_authors():
    top_three_authors = execute_query(query_top_authors)
    print ("\n" + "*** TOP AUTHORS ***")

    order = 1
    for name, viewCount in top_three_authors:
        print(str(order) + ". " + "\"" + name + "\"" +
              " -- " + str(viewCount) + " views.")
        order += 1


# Get the daays did more than 1% of requests lead to errors
def get_error_days():
    error_days = execute_query(query_errors)
    print ("\n" + "*** DAYS MORE THAN 1% OF REQUESTS LEAD TO ERRORS ***")

    for day, percent in error_days:
        print(str(day) + " -- " + str(percent * 100) + "% of requests.")

get_top_three_articles()
get_top_authors()
get_error_days()
