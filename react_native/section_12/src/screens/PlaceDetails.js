import { ScrollView, Image, View, Text, StyleSheet } from "react-native"
import OutlineButton from "../components/UI/OutlineButton"
import { Colors } from "../constants/colors"
import { useEffect, useState } from "react"
import { fetchPlaceDetails } from "../util/database"
import { Place } from "../models/place"


const PlaceDetails = ({ route, navigation }) => {

    const [fetchedPlace, setFechedPlace] = useState()
    const selectedPlaceId = route.params.placeId


    useEffect(() => {
        const loadPlaceDetails = async () => {
            const placeDetails = await fetchPlaceDetails(selectedPlaceId)
            const place = new Place(placeDetails.id,
                placeDetails.title,
                placeDetails.image_uri,
                { address: placeDetails.address, lat: placeDetails.lat, lng: placeDetails.lng }
            )
            setFechedPlace(place)
            navigation.setOptions({
                title: place.title,

            })

        }
        loadPlaceDetails()
    }, [selectedPlaceId])

    const showOnMapHandler = () => {
        navigation.navigate('Map', {initialLat: fetchedPlace.location.lat, initialLng: fetchedPlace.location.lng})
    }

    if (!fetchedPlace) {
        return <View><Text>Loading place data ... </Text></View>
    }

    return <ScrollView>
        <Image style={styles.image} source={{ uri: fetchedPlace?.imageUri }} />
        <View style={styles.location}>
            <View style={styles.addressContainer}>
                <Text style={styles.address}>{fetchedPlace?.address}</Text>
            </View>
            <OutlineButton icon='map' onPress={showOnMapHandler}>View on Map</OutlineButton>
        </View>
    </ScrollView>
}

const styles = StyleSheet.create({
    image: {
        height: '35%',
        minHeight: 300,
        width: '100%'
    },
    location: {
        justifyContent: 'center',
        alignItems: 'center'
    },
    addressContainer: {
        padding: 20
    },
    address: {
        color: Colors.primary500,
        textAlign: 'center',
        fontWeight: 'bold',
        fontSize: 16
    },
    fallback: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        color: Colors.primary50
    }
})

export default PlaceDetails