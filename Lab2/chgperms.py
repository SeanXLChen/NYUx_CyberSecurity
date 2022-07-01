import os, sys, stat

os.chmod("testfile.txt", stat.S_IWGRP | stat.S_IXGRP)

print("mode changed successfully!")