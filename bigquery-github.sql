WITH repos as (
  SELECT b.repo_with_stars as repo_name,
         b.stars as stars
  FROM (
    SELECT DISTINCT repo_name AS repo_in_mirror
    FROM `bigquery-public-data.github_repos.files` 
  ) a RIGHT JOIN (
    SELECT repo.name AS repo_with_stars, APPROX_COUNT_DISTINCT(actor.id) stars 
    FROM `githubarchive.year.2017` 
    WHERE type='WatchEvent'
    GROUP BY 1 
    HAVING stars > 300
  ) b
  ON a.repo_in_mirror = b.repo_with_stars
  WHERE
    a.repo_in_mirror IS NOT NULL
),
contents as (
  SELECT *
  FROM (
    SELECT DISTINCT *
    FROM `bigquery-public-data.github_repos.sample_files` 
    WHERE repo_name IN (SELECT repo_name FROM repos)
  ) a RIGHT JOIN (
    SELECT id as idcontent,
           content as content
    FROM `bigquery-public-data.github_repos.contents` 
  ) b
  ON a.id = b.idcontent 
)
SELECT repos.repo_name,
       repos.stars
FROM repos
JOIN
  contents
ON
  repos.repo_name = contents.repo_name 
WHERE
  contents.content LIKE '%junit</artifactId>%'
  AND contents.path LIKE 'pom.xml'
ORDER BY
  repos.stars DESC
LIMIT 100