import random

def main():
    if 0:
        Omega = [0,1,2,3,4,5,"dog","cat","horse","tiger","lion","cat"]
    elif 1:
        # https://www.washingtontimes.com/news/2019/feb/28/robert-mueller-probe-spurs-death-threats-financial/
        Omega = """Hours after Democrats accused Carter Page of being a Russian asset 
        at a 2017 hearing of the House Permanent Select Committee on Intelligence, 
        the former Trump campaign adviser received a chilling voicemail."""

    x = random.sample(Omega, 6)

    print(x) # ['s', 'C', '\n', 'a', 'b', 'a']

if __name__ == "__main__":
    main()