import Foundation

let MAX_RETRIES = 3

/// Represents a user model.
struct User {
    let id: Int
    let name: String
}

/// Status of a resource.
enum Status {
    case active
    case inactive
}

/// Handles user operations.
class UserService {
    /// Retrieves a user by id.
    func getUser(userId: Int) -> User? {
        return nil
    }

    /// Creates a new service.
    init(config: String) {
    }
}

extension UserService {
    /// Resets the service state.
    func reset() {
    }
}

/// Authenticate a token.
func authenticate(token: String) -> Bool {
    return !token.isEmpty
}

protocol Authenticatable {
    func authenticate(token: String) -> Bool
}
