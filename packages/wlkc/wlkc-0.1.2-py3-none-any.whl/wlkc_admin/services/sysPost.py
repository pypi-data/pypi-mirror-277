from wlkc_core.database import db_session
from wlkc_admin.modules.sys import Post, UserPost


def queryAllPosts():
    return [item.to_json() for item in Post.query.all()]


def queryPostByUserId(userId):
    if userId:
        return [item.post_id for item in UserPost.query.filter(UserPost.user_id == userId).all()]
    return []


def deleteUserPost(userIds):
    return db_session.query(UserPost).filter(UserPost.user_id.in_(userIds)).delete(synchronize_session=False)