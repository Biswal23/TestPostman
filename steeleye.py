import datetime as dt

from typing import Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI,Body
import uvicorn as uvicorn


app = FastAPI(debug=True)

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")

class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")



@app.put("/trade/{trade_id}")
def update_trade(Trade:str,trade:Trade = Body(embed=True)):
   results= (Trade)
   return results

@app.put("/trade1/{trade_id}")
def update_trade(trade_id:str, trade: Annotated[Trade, Body(embed=True)]):
   results= {"trade_id":trade_id,"trade":trade}
   return results

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


