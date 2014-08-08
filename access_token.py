
def get_token():
  f = open("token.txt", "r");
  token = "";
  for line in f:
    token = line.strip();
    break;
  return token;
