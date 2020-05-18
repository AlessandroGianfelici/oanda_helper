import matplotlib.pyplot as plt

#funzione per stampare plot
def plot_hist_prices(name, historical_prices):

        y = historical_prices[['openBid', 'openAsk']].values # li plotto entrambi per avere un'idea dello spread bid-ask, per capire se ci sono momenti della giornata in cui è più stretto
        x = historical_prices.reset_index()['time']

        fig, ax1 = plt.subplots(figsize=(10, 6))
        plt.title(name + ': historical prices')
        plt.xlabel('time')
        ax1.plot(x.values, y)
        #ax2 = ax1.twinx()
        #ax2.set_alpha(0.001)
        #ax2.bar(x.values, vol, color='lightblue',align='center', alpha=0.45)
        ax1.legend(['bid price', 'ask price'], loc='upper right')
        #ax1.set_ylabel('price')
        #ax2.set_ylabel('volume')
        plt.grid(True)
        plt.show()

        historical_prices['volume'].plot(figsize=(10, 6))
        ax1.set_ylabel('volume')
        plt.grid(True)
        plt.show()

        return None
