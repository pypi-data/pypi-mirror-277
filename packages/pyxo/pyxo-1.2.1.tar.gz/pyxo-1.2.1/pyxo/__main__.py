from pyxo.controler import Engin

def main():
    try:
        Engin().run()
    except KeyboardInterrupt:
        print("\n\nBye Bye")
        exit(0)

if __name__ == '__main__':
    main()