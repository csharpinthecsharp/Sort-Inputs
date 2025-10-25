import sys
from handlers import h_input
from debugs import d_time
def main():
    deb = d_time.Debug()
    if not h_input.handle_input(sys.argv):
        print("\nExit code: Error")
        return (False)
    deb.stop()
    print("\nExit code: Success")
    return (True)
    
if __name__ == "__main__":
    main()
