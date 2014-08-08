import facebook
import json
import fql;

def get_name_from_id(uid, token):
  query = "SELECT name FROM user WHERE uid="+str(uid);
  name_json = fql.get_json(query, token);
  name = name_json['data'];
  for n in name:
    return n['name'];

def get_detail_from_id(detail, uid, token):
  query = "SELECT" + detail + "FROM user WHERE uid="+str(uid);
  detail_json = fql.get_json(query, token);
  detail = detail_json['data'];
  for d in detail:
    return d[detail];
