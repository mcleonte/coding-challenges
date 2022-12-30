"""
Consider the following dataframe :

request_path |         search_term |  user_id |      ip_address |       date
----------------------------------------------------------------------------
      search | Saving Private Ryan | 09663ea6 |  168.196.83.238 | 2021-04-07
      search |   Fear and Loathing | 63f84e80 |    116.103.0.64 | 2021-04-07
      search |      Legally Blonde | 31c73683 |    9.47.206.231 | 2021-04-07
      search |      Legally Blonde | 010b4076 |   198.45.207.12 | 2021-04-07
      search | The Hills Have Eyes | 31c73683 | 248.212.242.192 | 2021-04-07
      search |          Knives Out | 8173164f |   65.166.90.163 | 2021-04-01
...

It represents user interactions with movie search pages. Each interaction is
represented by the user_id of the user who made it, the movie search term that
they looked for, and the date of the interaction, amongst other things.

Use this interaction dataframe, accessible as search_interaction_df in the code,
to create a features dataframe of the following form:

 user_id |month_interaction_count |week_interaction_count |day_interaction_count
--------------------------------------------------------------------------------
010b4076 |                     xx |                    xx |                   xx
31c73683 |                     xx |                    11 |                   xx
8173164f |                     30 |                    xx |                    2
f77ad2d3 |                     xx |                    xx |                    2
25050522 |                     xx |                     8 |                   xx
bfb27c75 |                     xx |                     8 |                    2
09663ea6 |                     xx |                    xx |                   xx
ca7aacf2 |                     xx |                     1 |                   xx
63f84e80 |                     xx |                    xx |                    3
cbb81ed7 |                     24 |                    xx |                   xx


Each user_id in the returned dataframe should have entries in the
month_interaction_count, week_interaction_count and day_interaction_count
columns representing the number of search page interactions that the user had
over the past month, week, and day, respectively.

The past month, week, and day should be based off of the latest date present in
search_interaction_df; specifically, they should be the last 30, 7, and 1 days
before the last date, respectively.
"""

from pyspark.sql import SparkSession


def get_user_interaction_counts(search_interaction_df):
  spark = SparkSession.builder.getOrCreate()
  search_interaction_df.createOrReplaceTempView("interactions")
  return spark.sql("""
    WITH cte AS (
      SELECT
        user_id,
        DATEDIFF(
          CAST(( MAX(date) OVER () ) AS DATE),
          CAST(date AS DATE)
        ) AS days_ago
      FROM interactions
    )
    SELECT user_id,
      SUM(IF(days_ago <= 30, 1, 0)) AS month_interaction_count,
      SUM(IF(days_ago <= 7, 1, 0)) AS week_interaction_count,
      SUM(IF(days_ago <= 1, 1, 0)) AS day_interaction_count
    FROM cte
    GROUP BY user_id
    """)
