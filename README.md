# Algorytm Dijkstry 
Repozytorium z pracą zaliczeniową z przedmiotu Teoria Grafów.
## Instrukcja działania 
W pliku *graph.txt* podawany jest graf w postaci macierzy sąsiedztwa. **Ostatnia linijka** pliku to wierzchołek startowy, dla którego będą obliczane ścieżki do poszczególnych wierzchołków. Projekt nie wymaga dodatkowej konfiguracji.
## Cel algorytmu Dijkstry
Algorytm Dijkstry wykorzystywany jest do znajdowania najkrótszych ścieżek do wszystkich wierzchołków w grafie od wybranego wierzchołka startowego. Warto zauważyć, iż wagi nie mogą być ujemne. 
## Zastosowania algorytmu Dijkstry 
- Google Maps:
Algorytm Dijkstry jest używany, aby znaleźć minimalną odległość między dwoma miejscami wzdłuż dróg.  
- Serwisy społecznościowe 
Na podstawie algorytmu Dijkstry może zostać ustalona potencjalna lista znajomych. Znajduje jednak to zastosowanie tylko dla małej liczby danych. Z większą ilością danych lepiej radzą sobie bardziej skomplikowane algorytmy.
- Routing IP
Protokołem wykorzystującym algorytm Dijkstry jest na przykład OSPF (Open Shortest Path First). Za jego pomocą znajdowana jest najlepsza ścieżka z routera źródłowego do docelowego. Używany jest również w innych protokołach wymagających okresowej aktualizacji tablicy routingu.
