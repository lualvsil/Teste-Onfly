"""Teste Criado: Teste de leitura do arquivo CSV de reservas."""

from helpers import run_cli

def test_reads_more_than_200_reservations(tmp_path):
    """O CLI deve ser capaz de lidar com arquivos com mais de 200 linhas."""
    reservations = [
        {"reservation_id": f"R-{id}", "currency": "BRL", "amount": "100.00"} for id in range(201)
    ]
    report = run_cli(
        tmp_path,
        reservations
    )
    
    assert report["summary"] == {
        "total_reservations": 201,
        "confirmed_reservations": 201,
        "cancelled_reservations": 0,
        "no_show_reservations": 0,
        "total_room_nights": 201,
        "total_amount_brl": "20100.00",
        "average_nightly_rate_brl": "100.00"
    }
