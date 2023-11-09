from typing import Dict


async def parser(row: Dict):
    profile = {}

    profile['name'] = ' '.join(filter(None, (row['first_name'], row['last_name'])))
    profile['username'] = ' '.join(filter(None, (row['username'],)))
    profile['photo'] = row['photo_id']

    return profile
