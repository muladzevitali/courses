import { useIsFocused } from "@react-navigation/native"
import PlacesList from "../components/Places/PlacesList"
import { useState, useEffect } from "react"
import { fetchPlaces } from "../util/database"
import { Place } from "../models/place"

const AllPlaces = ({ route }) => {
    const [places, setPlaces] = useState([])

    const isFocused = useIsFocused()

    useEffect(() => {
        const loadPlaces = async () => {
            const results = await fetchPlaces()
            const places = results.map(dp => new Place(dp.id, dp.title, dp.image_uri, { address: dp.address, lat: dp.lat, lng: dp.lng }))

            setPlaces(places)
        }
        if (isFocused) {
            loadPlaces()
        }

    }, [isFocused])

    return <PlacesList places={places} />
}

export default AllPlaces