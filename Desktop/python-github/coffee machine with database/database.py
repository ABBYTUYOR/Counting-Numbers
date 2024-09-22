from prettytable import PrettyTable
import psycopg2
import psycopg2.extras

menu  = [
        {
            'Espresso': {
            'Water': 50,
            'Coffee': 18,
            },
            'Cost': 1.5
        },
        {
          'Latte':{
            'Water': 200,
            'Coffee': 24,
             'Milk': 150,
          },
            'Cost': 2.5
        },
        {
            'Cappuccino':{
            'Water': 250,
            'Coffee': 24,
            'Milk': 100
            },
            'Cost': 3.0
        }
    ]

resources = [{
    'Water': 1000,
    'Coffee': 500,
    'Milk': 2000,
    'Money': 2.5
    }
]

def configuration():
    hostname = 'localhost'
    database = 'coffee_machine_resources'
    username = 'postgres'
    password = 1234
    port = 5432
    return psycopg2.connect(host=hostname, database=database, user=username, password=password, port=port)


def select_command():
    with configuration() as conn:
        with conn.cursor() as cur:

            select_script = 'SELECT * FROM inventory'
            cur.execute(select_script)

            report_table = PrettyTable()

            for list in cur.fetchall():
                report_table.add_column('Inventory', ['Water', 'Coffee', 'Milk', 'Money'])
                report_table.add_column('Total', [list[1], list[2], list[3], list[4]])

            print(report_table)

def update_command(water, coffee, milk):
    # replenish inventory by 500
    with configuration() as conn:
        with conn.cursor() as cur:

            update_script = 'UPDATE inventory SET water = %s, coffee = %s, milk = %s  WHERE id = 1'
            update_values = (water, coffee, milk)
            cur.execute(update_script, update_values)
            conn.commit()

            return print('\nInventory has been replenish 🔄\n')

def deduction_command(water, coffee, milk, money):
    with configuration() as conn:
        with conn.cursor() as cur:

            update_script = 'UPDATE inventory SET water = %s, coffee = %s, milk = %s, cash = %s  WHERE id = 1'
            update_values = (water, coffee, milk, money)
            cur.execute(update_script, update_values)
            conn.commit()

def resources_command():
    with configuration() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            select_script = 'SELECT water, coffee, milk, cash FROM inventory'
            cur.execute(select_script)

            resources_list = []

            for r in cur.fetchall():
                resources_list.append(r['water'])
                resources_list.append(r['coffee'])
                resources_list.append(r['milk'])
                resources_list.append(r['cash'])
            return resources_list


def connection_command():
    try:
        with configuration() as conn:

            with conn.cursor() as cur:

                drop_table_script = 'DROP TABLE IF EXISTS inventory'
                cur.execute(drop_table_script)

                create_script = 'CREATE TABLE IF NOT EXISTS inventory(id INT PRIMARY KEY, water INT, coffee INT, milk INT, cash FLOAT)'
                cur.execute(create_script)

                insert_script = 'INSERT INTO inventory(id, water, coffee, milk, cash) VALUES (%s, %s, %s, %s, %s)'
                #Coffee Machine Starting resources
                insert_values = (1, 300, 100, 200, 2.0)
                cur.execute(insert_script, insert_values)

                conn.commit()

    except psycopg2.Error as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
