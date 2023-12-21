using Iot.Device.OneWire;

bool flag = true;
Console.CancelKeyPress += (sender, eventArgs) =>
{
    flag = false;
};
while (flag)
{
    foreach (var dev in OneWireThermometerDevice.EnumerateDevices())
    {
        Console.WriteLine($"Name: {dev.DeviceId}");
        Console.WriteLine($"Temperature: {dev.ReadTemperature():g}");
        Console.WriteLine();
    }
}