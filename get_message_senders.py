import message_senders;
import sys;

senders = {};
def get_senders(filename):
  f = open(filename, "w");
  i=1;
  while(1):
    print "Querying for " + str(i) + " " + str(i+49);
    try:
      senders_dict = message_senders.get_fifty(i, i+49);
    except:
      print "Failed\n";
      i+=50;
      continue;
    i += 50;
    print "Received dictionary.\nProcessing....";
    if len(senders_dict.keys()) == 0:
      break;
    for key in senders_dict.keys():
      if key not in senders.keys():
        senders[key] = senders_dict[key];
    print "Finished processing dictionary";
  for key in senders.keys():
    try:
      f.write(senders[key] + "\t" + key + "\n");
    except(TypeError):
      sys.stderr.write("User not found - probably a group mesg\n");
  return;

get_senders("outfile");
