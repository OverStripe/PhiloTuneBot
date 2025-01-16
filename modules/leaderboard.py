import redis

# Connect to Redis (Leaderboard Database)
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

def update_user_play_count(user_id):
    redis_client.zincrby("user_leaderboard", 1, user_id)

def get_top_users():
    users = redis_client.zrevrange("user_leaderboard", 0, 4, withscores=True)
    return [{"user_id": u[0], "plays": int(u[1])} for u in users]

def get_user_rank(user_id):
    rank = redis_client.zrevrank("user_leaderboard", user_id)
    total_plays = redis_client.zscore("user_leaderboard", user_id)
    return {"rank": rank + 1 if rank is not None else "N/A", "total_plays": int(total_plays) if total_plays else 0}
