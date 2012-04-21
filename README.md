# WebGL API

This API surfaces data for use in the WebGL visualization. 

Results are returned in JSON. The general format is:

```json
[key, [[lat, lon, magnitude], ..., [lat, lon, magnitude]]
```

Example request for 10 fires with magnitude coming from the brightness column:

[http://ecohackfirez.appspot.com/api/webgl?count=10&mag=brightness](http://ecohackfirez.appspot.com/api/webgl?count=10&mag=brightness)

Description of URL parameters:

<table>
    <tr>
        <td><b>Parameter</b></td>
        <td><b>Description</b></td>
        <td><b>Example</b></td>
    </tr>
    <tr>
        <td>count</td>
        <td>Number of fires to return</td>
        <td10</td>
    </tr>
    <tr>
        <td>mag</td>
        <td>Magnitude of fire (brightness or confidence)</td>
        <td>confidence</td>
    </tr>
</table>

