from google.cloud import bigquery

def run_query():
    client = bigquery.Client()

    query = """
    SELECT
      l.name AS language,
      COUNT(*) AS num_repositories
    FROM
      `bigquery-public-data.github_repos.languages`,
      UNNEST(language) AS l
    WHERE
      l.name IS NOT NULL
    GROUP BY
      language
    ORDER BY
      num_repositories DESC
    LIMIT 10
    """

    print("Running query on BigQuery...\n")
    results = client.query(query).result()

    print(f"{'Language':<15} | {'Repositories':>12}")
    print("-" * 30)
    for row in results:
        print(f"{row.language:<15} | {row.num_repositories:>12}")

if __name__ == "__main__":
    run_query()
