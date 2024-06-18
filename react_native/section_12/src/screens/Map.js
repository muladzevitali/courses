import { useCallback, useLayoutEffect, useState } from "react"
import { StyleSheet, Alert } from "react-native"
import MapView, { Marker } from "react-native-maps"
import IconButton from "../components/UI/IconButton"


const Map = ({ navigation, route }) => {
    const initialLocation = route.params && { lat: route.params.initialLat, lng: route.params.initialLng }

    const [selectedLocation, setSelectedLocation] = useState(initialLocation)

    const region = {
        latitude: initialLocation ? initialLocation.lat : 41.73321,
        longitude: initialLocation ? initialLocation.lng : 44.780957,
        latitudeDelta: 0.0922,
        longitudeDelta: 0.0421
    }

    const selectLocationHandler = (event) => {
        const lat = event.nativeEvent.coordinate.latitude
        const lng = event.nativeEvent.coordinate.longitude

        setSelectedLocation(_ => ({ lat: lat, lng: lng }))
    }

    const savePickedLocationHander = useCallback(() => {
        if (!selectedLocation) {
            Alert.alert('No location picked', 'You have to pick location first')
            return
        }

        navigation.navigate('AddPlace', { pickedLat: selectedLocation.lat, pickedLng: selectedLocation.lng })
    }, [navigation, selectedLocation]
    )

    useLayoutEffect(() => {
        if (!initialLocation) {
            navigation.setOptions({
                headerRight: ({ tintColor }) => <IconButton icon='save' size={24} color={tintColor} onPress={savePickedLocationHander} />
            })
        }
    }, [navigation, savePickedLocationHander, initialLocation])

    return (
        <MapView style={styles.map}
            initialRegion={region}
            onPress={selectLocationHandler}
        >
            {selectedLocation &&
                <Marker
                    title='Picked location'
                    coordinate={{ latitude: selectedLocation.lat, longitude: selectedLocation.lng }}
                />}
        </MapView>
    )
}


const styles = StyleSheet.create({
    map: {
        flex: 1
    }
})

export default Map