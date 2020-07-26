
from googlebooks.GoogleBooks import GoogleBooks

if __name__ == "__main__":
    data = GoogleBooks()
    data.setCavName("Australia me")

    data.setSearch("Australia+me")

    data.setFromDate("1")
    data.setFromMonth("1")

    data.setToDate("31")
    data.setToMonth("12")

    for year in range(1900,2021):
        data.setFromYear(str(year))
        data.setToYear(str(year))
        data.doSearch()
        print(year)
    
    data.end()