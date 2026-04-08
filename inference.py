from env.environment import CustomerSupportEnv

env = CustomerSupportEnv()

total = 0

for _ in range(3):
    query = env.reset()

    print("Query:", query)

    # dummy AI response (simulate)
    answer = "Sorry, please check your order status or contact support for refund."

    print("Answer:", answer)

    _, reward, _, info = env.step(answer)

    print("Score:", reward, info)
    print("------------")

    total += reward

print("Final Score:", total/3)