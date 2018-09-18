import statistics
import time
from collections import defaultdict


# q1_p2.py


def main():
    f = open("prices_sample.csv","r")
    f_contents = f.read()
    f_list = f_contents.splitlines()
    date_price_f_dict = defaultdict(list)
    price_f_dict = defaultdict(list)
    for x in range(0,len(f_list)):

        tmp_price = int(f_list[x][11:])
        price_f_dict["prices"].append(int(tmp_price))

        tmp_date = f_list[x][:10]
        tmp_date = time.strftime("%Y-%m-%d %H:%M:S", time.localtime(int(tmp_date)))
        tmp_date = tmp_date[:10]
        date_price_f_dict[tmp_date].append(tmp_price)
    med_index = int(len(price_f_dict["prices"])/2)
    print("\nStatistics for prices_sample.csv")
    print("25th percentile: " + str(statistics.median(price_f_dict["prices"][0:med_index])))
    print("50th percentile: " + str(statistics.median(price_f_dict["prices"])))
    print("75th percentile: " + str(statistics.median(price_f_dict["prices"][med_index:])))
    print("Variance:        " + str(statistics.variance(price_f_dict["prices"])) + "\n")

    mean = statistics.mean(price_f_dict["prices"])
    mean_dict = {}
    for x in date_price_f_dict:
        mean_dict[x] = abs(statistics.mean(date_price_f_dict[x]) - mean)
    sortedMeans = sorted(mean_dict, key=mean_dict.get)
    greatest5Means = sortedMeans[-5:]
    print("Five Largest Outliers from the Mean (" + str(mean) + ")")
    for x in greatest5Means:
        print(x + ": " + str(statistics.mean(date_price_f_dict[x])))
    print("")


if __name__ == "__main__":
    main()
