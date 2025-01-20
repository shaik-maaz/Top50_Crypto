{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ed911ae8-78f5-485d-9d0c-b9d68782c0e6",
   "metadata": {},
   "source": [
    "# Fetching and Analyzing Top 50 Live Cryptocurrency Data\n",
    "**Objective:**\n",
    "The objective of this assessment is to fetch live cryptocurrency data for the top 50 cryptocurrencies, store it in a MySQL database, and analyze it by connecting the database to Power BI. The data will be dynamically updated and visualized in Power BI to present live cryptocurrency prices, market capitalization, 24-hour price changes, and trading volumes.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "672f4b5d-e4bd-45e3-953f-9a2dedf3d5c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "import mysql.connector\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7107f6cc-65de-4e27-8ff6-0740fe473d5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# configure mysql connection\n",
    "db_config={\n",
    "    'host' : 'localhost',\n",
    "    'port': 3307,\n",
    "    'user': 'root',          # replace with your username\n",
    "    'password': '********', # replace with your password\n",
    "    'database': 'crypto_data'\n",
    "}\n",
    "# establish connection\n",
    "connection = mysql.connector.connect(**db_config)   \n",
    "cursor = connection.cursor()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "87436e28-ec85-400d-a9bb-032de6fdbcb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table created successfully!\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# create a table if it doesn't exist\n",
    "create_table_query =\"\"\" \n",
    "CREATE TABLE IF NOT EXISTS cryptocurrency (\n",
    "    id INT AUTO_INCREMENT PRIMARY KEY,\n",
    "    name VARCHAR(255),\n",
    "    symbol VARCHAR(255),\n",
    "    current_price FLOAT,\n",
    "    market_cap FLOAT,\n",
    "    trading_vol_24hr FLOAT,\n",
    "    price_change_percent FLOAT,\n",
    "    high_24hr FLOAT,\n",
    "    low_24hr FLOAT,\n",
    "    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP \n",
    "    );\n",
    "    \"\"\"\n",
    "cursor.execute(create_table_query)\n",
    "connection.commit()   \n",
    "\n",
    "print(\"Table created successfully!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8591b91a-d7f9-492b-818f-d061bd8c397f",
   "metadata": {},
   "source": [
    "**To fetch the data from CoinGecko API**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0d16af3a-b33d-4f17-984f-8e50a1a2f40d",
   "metadata": {},
   "outputs": [],
   "source": [
    "url='https://api.coingecko.com/api/v3/coins/markets'\n",
    "parameters={'vs_currency':'usd','order':'market_cap_desc','per_page': 50 ,'page':1,'sparkline':'false'}\n",
    "\n",
    "response = requests.get(url,params=parameters)\n",
    "crypto_data= response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6a6ea8ab-b690-4c8f-9341-a6adcf077cf5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'id': 'bitcoin',\n",
       "  'symbol': 'btc',\n",
       "  'name': 'Bitcoin',\n",
       "  'image': 'https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png?1696501400',\n",
       "  'current_price': 107510,\n",
       "  'market_cap': 2131990833682,\n",
       "  'market_cap_rank': 1,\n",
       "  'fully_diluted_valuation': 2131990833682,\n",
       "  'total_volume': 122701305612,\n",
       "  'high_24h': 108786,\n",
       "  'low_24h': 99702,\n",
       "  'price_change_24h': 2528.43,\n",
       "  'price_change_percentage_24h': 2.40845,\n",
       "  'market_cap_change_24h': 52046544768,\n",
       "  'market_cap_change_percentage_24h': 2.5023,\n",
       "  'circulating_supply': 19812693.0,\n",
       "  'total_supply': 19812693.0,\n",
       "  'max_supply': 21000000.0,\n",
       "  'ath': 108786,\n",
       "  'ath_change_percentage': -1.28419,\n",
       "  'ath_date': '2025-01-20T09:11:54.494Z',\n",
       "  'atl': 67.81,\n",
       "  'atl_change_percentage': 158269.11882,\n",
       "  'atl_date': '2013-07-06T00:00:00.000Z',\n",
       "  'roi': None,\n",
       "  'last_updated': '2025-01-20T14:49:08.689Z'},\n",
       " {'id': 'ethereum',\n",
       "  'symbol': 'eth',\n",
       "  'name': 'Ethereum',\n",
       "  'image': 'https://coin-images.coingecko.com/coins/images/279/large/ethereum.png?1696501628',\n",
       "  'current_price': 3340.1,\n",
       "  'market_cap': 402928870862,\n",
       "  'market_cap_rank': 2,\n",
       "  'fully_diluted_valuation': 402928870862,\n",
       "  'total_volume': 63315010096,\n",
       "  'high_24h': 3439.78,\n",
       "  'low_24h': 3151.39,\n",
       "  'price_change_24h': -20.292292062295473,\n",
       "  'price_change_percentage_24h': -0.60387,\n",
       "  'market_cap_change_24h': -1953516438.1210327,\n",
       "  'market_cap_change_percentage_24h': -0.48249,\n",
       "  'circulating_supply': 120501725.2119089,\n",
       "  'total_supply': 120501725.2119089,\n",
       "  'max_supply': None,\n",
       "  'ath': 4878.26,\n",
       "  'ath_change_percentage': -31.57842,\n",
       "  'ath_date': '2021-11-10T14:24:19.604Z',\n",
       "  'atl': 0.432979,\n",
       "  'atl_change_percentage': 770788.20659,\n",
       "  'atl_date': '2015-10-20T00:00:00.000Z',\n",
       "  'roi': {'times': 40.535429593445734,\n",
       "   'currency': 'btc',\n",
       "   'percentage': 4053.5429593445733},\n",
       "  'last_updated': '2025-01-20T14:49:06.160Z'}]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# verifying the fetched data\n",
    "crypto_data[:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "66cbea09-98da-4e04-858b-52333d2d3d14",
   "metadata": {},
   "outputs": [],
   "source": [
    "# now we only pick the data we want"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f132f81-122e-42a2-95c3-552c5a097f2f",
   "metadata": {},
   "source": [
    "**Insert the data to Mysql Database**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7fca90c2-cae0-4852-ab4d-becbc80bf874",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data inserted successfully!\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# now insert the data into table\n",
    "insert_query= \"\"\"\n",
    "INSERT INTO cryptocurrency(name,symbol,current_price,market_cap,trading_vol_24hr,price_change_percent,high_24hr,low_24hr) \n",
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)\n",
    "\"\"\"\n",
    "for item in crypto_data:\n",
    "    cursor.execute(insert_query,(\n",
    "        item['name'],\n",
    "        item['symbol'],\n",
    "        item['current_price'],\n",
    "        item['market_cap'],\n",
    "        item['total_volume'],\n",
    "        item['price_change_percentage_24h'],\n",
    "        item['high_24h'],\n",
    "        item['low_24h']\n",
    "    ))\n",
    "\n",
    "connection.commit()\n",
    "\n",
    "print(\"Data inserted successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f77dce8e-2c65-4cc1-a310-5fae3e8e45f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 'Bitcoin', 'btc', 105176.0, 2083750000000.0, 48665100000.0, 2.06723, 105256.0, 102214.0, datetime.datetime(2025, 1, 19, 12, 6, 50))\n",
      "(2, 'Ethereum', 'eth', 3293.39, 396865000000.0, 32122600000.0, -0.78666, 3368.16, 3238.04, datetime.datetime(2025, 1, 19, 12, 6, 50))\n",
      "(3, 'XRP', 'xrp', 3.21, 184704000000.0, 8842640000.0, 2.36474, 3.28, 3.08, datetime.datetime(2025, 1, 19, 12, 6, 50))\n",
      "(4, 'Tether', 'usdt', 0.998697, 138176000000.0, 58587600000.0, -0.07845, 0.999673, 0.998762, datetime.datetime(2025, 1, 19, 12, 6, 50))\n",
      "(5, 'Solana', 'sol', 269.93, 131570000000.0, 26542900000.0, 15.4345, 272.96, 232.06, datetime.datetime(2025, 1, 19, 12, 6, 50))\n"
     ]
    }
   ],
   "source": [
    "# Query the data\n",
    "cursor.execute(\"SELECT * FROM cryptocurrency\")\n",
    "rows = cursor.fetchall()\n",
    "\n",
    "# Display the results\n",
    "i=0\n",
    "for row in rows:\n",
    "    if i <5:\n",
    "        print(row)\n",
    "        i+=1\n",
    "    else:\n",
    "        break\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1e2940e-e4ff-4078-ba8d-2fbc55734203",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "323af7c0-9d52-4cde-91ee-d8239f75c260",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99ab62a1-4fc1-48df-91bb-727042975b48",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
