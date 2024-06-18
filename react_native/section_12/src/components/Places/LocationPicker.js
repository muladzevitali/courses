import { Alert, Image, StyleSheet, View, Text } from "react-native"
import OutlineButton from "../UI/OutlineButton"
import { Colors } from "../../constants/colors"
import { getCurrentPositionAsync, useForegroundPermissions, PermissionStatus } from "expo-location"
import { useState, useEffect } from "react"
import { getAddress, getMapPreview } from "../../util/location"
import { useNavigation, useRoute, useIsFocused } from "@react-navigation/native"


const LocationPicker = ({ onPickLocation }) => {
    const [pickedLocation, setPickedLocation] = useState()
    const [locationPermissionInformation, requestPermission] = useForegroundPermissions()

    const navigation = useNavigation()
    const route = useRoute()
    const isFocused = useIsFocused()

    useEffect(() => {
        if (isFocused && route.params) {
            setPickedLocation(_ => ({ lat: route.params.pickedLat, lng: route.params.pickedLng }))
        }
    }, [route, isFocused])

    useEffect(() => {
        const handleLocation = async () => {
            if (pickedLocation) {
                const address = await getAddress(pickedLocation.lat, pickedLocation.lng)
                onPickLocation({ ...pickedLocation, address: address })
            }
        }
        handleLocation()
    }, [pickedLocation, onPickLocation])

    const verifyPermissions = async () => {
        if (locationPermissionInformation.status === PermissionStatus.UNDETERMINED) {
            const permissionResponse = await requestPermission()
            return permissionResponse.status
        } else if (locationPermissionInformation.status === PermissionStatus.DENIED) {
            Alert.alert('Insufficient Permissions', 'You need to grant location permissions to use this app')
            return false
        }

        return true
    }

    const getLocationHandler = async () => {
        const isGranted = await verifyPermissions()
        if (!isGranted) {
            return
        }

        const location = await getCurrentPositionAsync()
        setPickedLocation(_ => ({ lat: location.coords.latitude, lng: location.coords.longitude }))
    }

    const pickOnMapHandler = () => {
        navigation.navigate('Map')
    }

    let mapPreview = <Text>No image taken yet</Text>

    if (pickedLocation) {
        console.log(getMapPreview(pickedLocation.lat, pickedLocation.lng))
        mapPreview = <Image source={{ uri: getMapPreview(pickedLocation.lat, pickedLocation.lng) }} style={styles.image} />
    }

    return (
        <View>
            <View style={styles.mapPreview}>
                {mapPreview}
            </View>
            <View style={styles.actions}>
                <OutlineButton icon='location' onPress={getLocationHandler}> Locate user </OutlineButton>
                <OutlineButton icon='map' onPress={pickOnMapHandler}> Pick on map</OutlineButton>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    mapPreview: {
        width: '100%',
        height: 200,
        marginVertical: 8,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: Colors.primary100,
        borderRadius: 4
    },
    actions: {
        flexDirection: 'row',
        justifyContent: 'space-around',
        alignItems: 'center'
    },
    image: {
        width: '100%',
        height: '100%',
    }
})

export default LocationPicker