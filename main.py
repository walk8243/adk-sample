import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

def main():
    logging.info("Hello from adk-sample!")


if __name__ == "__main__":
    main()
