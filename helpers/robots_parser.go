func getRobotsTxt(url string) (*robotstxt.RobotsData, error) {
    resp, err := httpClient.Get(url + "/robots.txt")
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        return nil, err
    }
    robots, err := robotstxt.FromBytes(body)
    if err != nil {
        return nil, err
    }
    return robots, nil
}