import sys
from handlers import h_input
from debugs import d_time
def main():
    deb = d_time.Debug()
    h_input.handle_input(sys.argv)
    deb.stop()
    
if __name__ == "__main__":
    main()
