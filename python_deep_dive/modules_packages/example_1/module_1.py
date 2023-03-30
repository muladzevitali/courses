print(f"-------running {__name__}")


def pprint(header, d):
    print('\n\n')
    print(header)
    for k, v in d.items():
        print(f"{k}: {v}")
    print('---------')


pprint('module_1.globals', globals())

print(f"-------end of {__name__}-------")

