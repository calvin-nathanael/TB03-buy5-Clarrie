import api, cash_on_hand, overheads, profit_loss

# modular program, ensure that the current working directory is project_group, not its parent folder!
def main():
    forex = api.api_function()
    overheads.overheads_function(forex)
    cash_on_hand.coh_function(forex)
    profit_loss.profitloss_function(forex)

main()
