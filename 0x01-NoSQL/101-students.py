#!/usr/bin/env python3
""" Top students """


def top_students(mongo_collection):
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {"_id": "$_id", "averageScore": {"$avg": "$scores.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    result = mongo_collection.aggregate(pipeline)
    return list(result)
