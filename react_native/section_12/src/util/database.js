import * as SQLite from "expo-sqlite"


export const init = async () => {
    const database = await SQLite.openDatabaseAsync('database.db', { useNewConnection: true })
    return await database.execAsync(`CREATE TABLE IF NOT EXISTS places (
        id INTEGER PRIMARY KEY NOT NULL,
        title TEXT NOT NULL,
        image_uri TEXT NOT NULL,
        address TEXT NOT NULL,
        lat REAL NOT NULL,
        lng REAL NOT NULL
    )`)
}

export const insertPlace = async (place) => {
    const database = await SQLite.openDatabaseAsync('database.db', { useNewConnection: true })

    return await database.runAsync(`INSERT INTO places (title, image_uri, address, lat, lng) VALUES (?, ?, ?, ?, ?)`, place.title, place.imageUri, place.address, place.location.lat, place.location.lng)
}

export const fetchPlaces = async () => {
    const database = await SQLite.openDatabaseAsync('database.db', { useNewConnection: true })
    const results = await database.getAllAsync('SELECT * FROM places')

    return results
}

export const fetchPlaceDetails = async (placeId) => {
    const database = await SQLite.openDatabaseAsync('database.db', { useNewConnection: true })
    const result = await database.getFirstAsync(`SELECT * FROM places where id=${placeId}`)

    return result
}