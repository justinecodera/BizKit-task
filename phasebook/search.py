from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    if not args:
        return USERS

    #this was my first iteration before the bonus question
    # result = set()

    # if 'id' in args:
    #     user_id = args['id']
    #     for user in USERS:
    #         if user['id'] == user_id:
    #             result.add(tuple(user.items()))  
    #             break  

    # if 'name' in args:
    #     name = args['name'].lower()
    #     for user in USERS:
    #         if name in user['name'].lower():
    #             result.add(tuple(user.items()))

    # if 'age' in args:
    #     try:
    #         age = int(args['age'])
    #         for user in USERS:
    #             user_age = int(user['age'])
    #             if age - 1 <= user_age <= age + 1:
    #                 result.add(tuple(user.items()))
    #     except ValueError:
    #         pass  

    # if 'occupation' in args:
    #     occupation = args['occupation'].lower()
    #     for user in USERS:
    #         if occupation in user['occupation'].lower():
    #             result.add(tuple(user.items()))

    # result = [dict(user) for user in result]
    # result.sort(key=lambda user: user['id'])

    # return result

    result = []
    added_ids = set()

    if 'id' in args:
        user_id = args['id']
        for user in USERS:
            if user['id'] == user_id and user['id'] not in added_ids:
                result.append(user)
                added_ids.add(user['id'])
                break  

    if 'name' in args:
        name = args['name'].lower()
        for user in USERS:
            if name in user['name'].lower() and user['id'] not in added_ids:
                result.append(user)
                added_ids.add(user['id'])

    if 'age' in args:
        try:
            age = int(args['age'])
            for user in USERS:
                user_age = int(user['age'])
                if age - 1 <= user_age <= age + 1 and user['id'] not in added_ids:
                    result.append(user)
                    added_ids.add(user['id'])
        except ValueError:
            pass 

    if 'occupation' in args:
        occupation = args['occupation'].lower()
        for user in USERS:
            if occupation in user['occupation'].lower() and user['id'] not in added_ids:
                result.append(user)
                added_ids.add(user['id'])

    # im using this to sort the users
    # result.sort(key=lambda user: user['id']) 

    return result
