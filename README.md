
<div align="center">
    <a href="https://github.com/RedisVentures/redis-vecsim"><img src="img/redis-logo.png" width="30%"><img></a>
    <br />
    <br />
<div display="inline-block">
    <a href="https://ecommerce.redisventures.com"><b>eCommerce Demo</b></a>&nbsp;&nbsp;&nbsp;
    <a href="https://docsearch.redisventures.com"><b>Docsearch Demo</b></a>&nbsp;&nbsp;&nbsp;
    <a href="https://redis.io/docs/stack/search/reference/vectors/"><b>Redis VSS Documentation</b></a>&nbsp;&nbsp;&nbsp;
  </div>
    <br />
    <br />
</div>

# Getting Started: **Redis Vector Similarity**
This entry-level tutorial is meant to guide you through:
- Setting up a RediSearch + Jupyter docker stack
- Creating text-based embeddings (vectors) from a sample/toy dataset
- Storing vector data in RediSearch
- Running vector queries and hybrid queries

___

**WARNING -- this is a toy example/demo**. This is not meant to replicate production in any way. Rather, use this to learn the basics to apply to your own data and pipelines.

## Docker Setup
Make sure you have Docker Desktop installed on your workstation.

Run this command to start up the stack of services including Redis and Jupyter:
```bash
$ docker compose up
```

Run this command to tear down the stack:
```bash
$ docker compose down
```

If at any point you need to trouble shoot, run this command to check running docker processes:
```bash
$ docker ps -a
```

Check logs of a docker container with the id found in last step:
```bash
$ docker logs {CONTAINER_ID} -f
```

## Jupyter Notebooks
We use Jupyter notebooks here to guide through the tutorial.

After running the `docker compose up` step, you should see a link in the logs like this:

![jupyter](img/jupyter_startup.png)

Use the last URL listed... the one that has your own custom token -- not this exact one :)


