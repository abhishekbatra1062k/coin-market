import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DataTable = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/get-coins-data');
        setData(response.data.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
    const intervalId = setInterval(fetchData, 3000);
    return () => clearInterval(intervalId);
  }, []);
  return (
    <div>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"></link>
      <h1>Crypto Coins Data</h1>
      <table class="table">
        <thead>
          <tr>
            <th>Rank</th>
            <th>Name</th>
            <th>Symbol</th>
            <th>Price</th>
            <th>1Hr Change</th>
            <th>24Hr Change</th>
            <th>7D Change</th>
            <th>Market Cap</th>
            <th>Volume 24Hr</th>
            <th>Circulating Supply</th>
          </tr>
        </thead>
        <tbody>
          {data.map(item => (
            <tr key={item.id}>
              <td>{item.rank}</td>
              <td>{item.name}</td>
              <td>{item.symbol}</td>
              <td>{item.price}</td>
              <td>{item.one_hour_change}</td>
              <td>{item.twenty_four_hour_change}</td>
              <td>{item.seven_day_change}</td>
              <td>{item.market_cap}</td>
              <td>{item.volume_24h}</td>
              <td>{item.circulating_supply}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
export default DataTable;