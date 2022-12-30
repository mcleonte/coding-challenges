-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/discuss/2825169/MySQL-or-Single-WHERE-clause%3A-DATEDIFF-...-BETWEEN-0-AND-29
SELECT
    activity_date as day,
    COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE DATEDIFF('2019-07-27',activity_date) BETWEEN 0 AND 29
GROUP BY day
