import sys
from handlers import h_input
def main():
    if not h_input.handle_input(sys.argv):
        print("\nExit code: Error")
        return (False)
    print("\nExit code: Success")
    return (True)
    
if __name__ == "__main__":
    main()
