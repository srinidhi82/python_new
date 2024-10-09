def order_summary(*prices, **addons):
  total = 0
  for price in prices:
    total+= price
    net_spend = total - addons['discount'] * total - addons['cashback']

    if total >= 10000:
      rewards = 800

    elif total >= 5000:
      rewards = 400

    elif total >= 1000:
      rewards = 200

    else:
      rewards = 0

  return total, net_spend, rewards

addons = {'discount': 0.10, 'cashback': 5}
ts, ns, rp = order_summary(19000,700,900, **addons)
print("Customer order summary:\n", "\ntotal:", ts, "\nnetspend:", ns, "\nrewards:", rp)