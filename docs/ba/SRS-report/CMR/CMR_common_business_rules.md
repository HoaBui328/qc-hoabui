# QUY TẮC NGHIỆP VỤ CHUNG (COMMON BUSINESS RULES - CMR)

## Phân hệ Báo cáo | Hệ thống MBFS

> Tài liệu này định nghĩa các quy tắc nghiệp vụ chung áp dụng xuyên suốt toàn bộ phân hệ Báo cáo.

---

## CMR_01: Thực thể lập báo cáo (ĐTNN/ĐTTN)

Dự án bắt buộc phải thành lập/chỉ định một **Tổ chức kinh tế (TCKT)** phụ trách toàn bộ việc lập và nộp báo cáo.

**Phân quyền theo đối tượng:**

| Đối tượng                             | Quyền được phép                                                              | Ghi chú UI                                                                                                    |
| :---------------------------------------- | :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **TCKT phụ trách**                | Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo                      | —                                                                                                             |
| **NĐT thành viên trong dự án** | **Chỉ Xem (view-only)** — không thấy nút Tạo, Chỉnh sửa, Xóa, Nộp | Bản ghi hiển thị ℹ️ kèm Tooltip:*"Báo cáo được lập bởi [Tên TCKT]"*. Tham chiếu: CS_01 Mục 5 |

---

## CMR_02: Thực thể lập báo cáo (ĐTRNN)

Dự án không có tổ chức phụ trách chung. Một NĐT bất kỳ trong dự án có thể đứng ra khởi tạo bản ghi báo cáo; sau khi bản ghi đã tồn tại, **tất cả NĐT trong dự án có quyền ngang nhau** trên bản ghi đó.

**Phân quyền theo đối tượng:**

| Đối tượng                                 | Quyền được phép                                                                                                                                               |
| :-------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NĐT khởi tạo bản ghi**            | Xem, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo                                                                                                                  |
| **Các NĐT khác trong cùng dự án** | **Đủ quyền như người khởi tạo** — Xem, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo *(nếu bản ghi thỏa điều kiện trạng thái theo CMR_03)* |

| Tiêu chí                       | Quy tắc                                                                                                                                                                   |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Một bản ghi duy nhất mỗi kỳ | Hệ thống chỉ tồn tại**01 bản ghi báo cáo** cho mỗi dự án/kỳ. Các NĐT cùng thao tác trên cùng 1 bản ghi này                                       |
| Ghi nhận vào Lifecycle Log     | Mọi thao tác của bất kỳ NĐT nào (Lập, Sửa, Nộp, Nhập từ file) đều được ghi vào Lifecycle Log kèm Tên NĐT và Thời gian. Tham chiếu: CF_06           |
| UI Danh sách                    | NĐT không phải người lập báo cáo: bản ghi hiển thị ℹ️ kèm Tooltip:*"Báo cáo được lập bởi NĐT [Tên NĐT khác]"*. Tham chiếu: CS_01 Mục 5        |
| Xung đột đồng thời          | Nếu 2 NĐT cùng mở chỉnh sửa và lưu cùng lúc, hệ thống áp dụng**Last Write Wins** — thao tác sau ghi đè. Cả 2 đều được ghi vào Lifecycle Log |

---

## CMR_03: Hành động theo từng trạng thái (người khởi tạo)

Hệ thống chỉ hiển thị/cho phép hành động tương ứng với từng trạng thái bản ghi:

| Trạng thái                      | Hành động được phép                                                                                                             | Ghi chú                                   |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
| **[Lưu nháp]**            | [Nộp], [Chỉnh sửa], [Xóa]*(chỉ khi chưa từng nộp — xem CF_08)*, [Xem chi tiết], [Xem vòng đời], [In], [Xuất báo cáo] | —                                         |
| **[Chờ duyệt]**           | [Xem chi tiết], [Xem vòng đời], [In], [Xuất báo cáo]                                                                            | Khóa quyền Nộp/Sửa/Xóa — vĩnh viễn |
| **[Đã tiếp nhận]**      | [Xem chi tiết], [Xem vòng đời], [In], [Xuất báo cáo]                                                                            | Khóa quyền Nộp/Sửa/Xóa — vĩnh viễn |
| **[Yêu cầu chỉnh sửa]** | [Nộp]*(Disabled khi chưa chỉnh sửa — xem CMR_14)*, [Chỉnh sửa], [Xem chi tiết], [Xem vòng đời], [In], [Xuất báo cáo]   | Không có [Xóa]. Tham chiếu: CF_09      |

**Quy tắc chuyển trạng thái khi Nộp:**

| Điều kiện                                                       | Trạng thái sau khi Nộp    |
| :----------------------------------------------------------------- | :--------------------------- |
| Quy trình**2 bước** (VD: Nộp → Tiếp nhận)             | **[Đã tiếp nhận]** |
| Quy trình**> 2 bước** (VD: Nộp → Duyệt → Tiếp nhận) | **[Chờ duyệt]**      |

---

## CMR_04: Trạng thái kỳ hạn báo cáo (Period Level)

Hệ thống quản lý trạng thái hiển thị theo từng kỳ hạn báo cáo, dựa vào realtime để so sánh kỳ hạn:

| Trạng thái      | Quy tắc                                                                               |
| :---------------- | :------------------------------------------------------------------------------------- |
| Chưa tới hạn   | Ẩn nút [Lập báo cáo] và [Nhập từ file]. Không cho phép tạo mới hoặc nhập |
| Trong thời hạn  | Hiển thị nút [Lập báo cáo] và [Nhập từ file]. Cho phép tạo mới và nhập   |
| Qua kỳ báo cáo | Ẩn nút [Lập báo cáo] và [Nhập từ file]. Không cho phép cho kỳ đã qua      |

---

## CMR_05: Quy tắc trường Số (Numeric Fields)

Áp dụng cho toàn bộ trường nhập liệu dạng số.

### 5.0. Cơ chế Validation chung (Global Rule)

| Tiêu chí      | Quy tắc                                                                                                   |
| :-------------- | :--------------------------------------------------------------------------------------------------------- |
| Trigger         | Kiểm tra**ngay khi người dùng gõ phím hoặc paste** dữ liệu                                  |
| Action khi lỗi | Hiển thị Inline Error Message màu đỏ ngay lập tức bên dưới trường + highlight đỏ viền field |

**Thứ tự ưu tiên hiển thị lỗi** — Khi chuỗi vi phạm nhiều rule, chỉ hiển thị **1 thông báo lỗi ưu tiên cao nhất**:

1. **(Ưu tiên 1)** Bỏ trống trường bắt buộc (Required — nếu có)
2. **(Ưu tiên 2)** Sai định dạng (chứa ký tự không hợp lệ, thừa dấu thập phân, sai vị trí dấu phân cách)
3. **(Ưu tiên 3)** Vi phạm giới hạn độ dài (min/max-length, vượt quá số chữ số phần nguyên/thập phân)

### 5.1. Kiểm tra định dạng số (Dấu chấm, Dấu phẩy)

| Tiêu chí                         | Quy tắc                                                                                                                                                      | Error Message                                                            |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------- |
| Ký tự hợp lệ (số thập phân) | Chữ số (`0-9`), dấu trừ (`-`), dấu chấm (`.`), dấu phẩy (`,`)                                                                                 | Nhập ký tự ngoài danh sách →*"Định dạng số không hợp lệ"* |
| Ký tự hợp lệ (số nguyên)     | Chữ số (`0-9`), dấu trừ (`-`), dấu phẩy (`,`). Không cho phép dấu chấm (`.`)                                                                | Nhập ký tự ngoài danh sách →*"Định dạng số không hợp lệ"* |
| Ký tự hợp lệ (số dương)     | Chữ số (`0-9`), dấu chấm (`.`), dấu phẩy (`,`). Không cho phép dấu trừ (`-`)                                                                | Nhập `-` → *"Định dạng số không hợp lệ"*                    |
| Thừa dấu thập phân             | Báo lỗi ngay khi gõ dấu chấm thứ 2. VD:`1.1.1` hoặc `1.1.1,777`                                                                                    | *"Định dạng số không hợp lệ"*                                   |
| Sai vị trí dấu phẩy            | Dấu phẩy phải phân tách đúng nhóm 3 chữ số phần nguyên; không được xuất hiện sau dấu chấm. VD:`1,1,1` hoặc `1.23,3333` hoặc `1.,` | *"Định dạng số không hợp lệ"*                                   |
| Dấu trừ sai vị trí             | Dấu trừ chỉ được nằm ở vị trí đầu tiên                                                                                                           | *"Định dạng số không hợp lệ"*                                   |
| Trường số dương (>= 0)        | Không cho phép nhập dấu trừ.*(Áp dụng khi UC SRS quy định rõ trường không cho phép số âm.)*                                                 | *"Định dạng số không hợp lệ"*                                   |

### 5.2. Giới hạn độ dài

| Tiêu chí                       | Quy tắc                                                                                                                                                                                                     | Error Message                                                                                                         |
| :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| Số thập phân                  | Tối đa**15 chữ số phần nguyên** và **5 chữ số phần thập phân** (Tổng cộng 21 ký tự bao gồm cả dấu `.`). Vượt quá giới hạn ở bất kỳ phần nào đều báo lỗi chung | Vượt →*"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"* |
| Số nguyên (không thập phân) | Tối đa**15 ký tự**                                                                                                                                                                                 | Vượt →*"[Tên trường] không được vượt quá [maxlength] ký tự!"*                                        |
| Ưu tiên UC riêng              | Nếu UC SRS quy định max length riêng → ưu tiên theo UC                                                                                                                                                | —                                                                                                                    |
| Copy/Paste vượt max            | Hệ thống giữ nguyên toàn bộ chuỗi,**KHÔNG tự cắt nội dung**, báo lỗi ngay lập tức                                                                                                       | Tùy loại vi phạm (xem 5.1 và 5.2)                                                                                 |
| Chưa đủ min length            | Nếu UC SRS quy định min length                                                                                                                                                                            | *"[Tên trường] nhập chưa đủ [minlength] ký tự!"*                                                           |

### 5.3. UX Auto-format (tự động, KHÔNG báo lỗi)

| Tiêu chí                               | Quy tắc                                                                                                       |
| :--------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| Leading Zero (số 0 đầu phần nguyên) | Tự động xóa số 0 đầu khi gõ chữ số thứ 2. VD: gõ `0` rồi `9` → hiển thị `9`              |
| Trailing Zero (số 0 cuối thập phân)  | Không can thiệp khi đang gõ. Chỉ tự cắt khi**out-click**. VD: `999.000` → out-click → `999` |
| Khoảng trắng đầu/cuối               | Không can thiệp khi đang gõ. Tự động xóa khi**out-click**                                        |
| Bắt đầu bằng dấu `.`              | Tự động chèn `0` phía trước. VD: gõ `.9` → hiển thị `0.9`                                     |

### 5.4. Validate khi Copy/Paste vào trường Số

| Tiêu chí                          | Quy tắc                                                                                                                                                    | Error Message                                                                                                |
| :---------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| Nguyên tắc chung                  | Khi Paste, hệ thống**KHÔNG tự động lọc hay xóa** bất kỳ ký tự nào. Giữ nguyên toàn bộ chuỗi, kiểm tra real-time và báo lỗi ngay | —                                                                                                           |
| Paste chứa ký tự không hợp lệ | VD: Paste `1234kdjrh123` → Giữ nguyên chuỗi                                                                                                           | *"Định dạng số không hợp lệ"*                                                                       |
| Paste vượt giới hạn thập phân | VD: Paste `1234567890123456.839485` → Giữ nguyên chuỗi                                                                                                | *"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"* |
| Paste sai vị trí dấu phẩy       | VD: Paste `1,2,3,4,5` → Giữ nguyên chuỗi                                                                                                              | *"Định dạng số không hợp lệ"*                                                                       |
| Paste sai dấu liền kề            | VD: Paste `2..345,8493` → Giữ nguyên chuỗi                                                                                                            | *"Định dạng số không hợp lệ"*                                                                       |

### 5.5. Placeholder & Trường bắt buộc

| Tiêu chí                         | Quy tắc                                                                         | Error Message                         |
| :--------------------------------- | :------------------------------------------------------------------------------- | :------------------------------------ |
| Placeholder                        | *"Nhập [tên trường]"* (VD: *"Nhập số tiền"*, *"Nhập số lượng"*) | —                                    |
| Trường bắt buộc bị bỏ trống | Hiển thị lỗi inline, tự biến mất khi nhập hợp lệ                        | *"Vui lòng nhập [tên trường]"* |

---

## CMR_06: Quy tắc Trường Text / Textarea / Ô tìm kiếm

Áp dụng cho toàn bộ trường Textbox, Textarea và Search box:

### 6.1. Auto trim & Khoảng trắng

| Tiêu chí                | Quy tắc                                                                                                                                 |
| :------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Auto trim                 | Tự động xóa khoảng trắng đầu/cuối khi**out-click (blur)**. Trong lúc đang gõ, giữ nguyên để không ảnh hưởng UX |
| Chỉ nhập khoảng trắng | Hệ thống coi là không có dữ liệu (tương đương rỗng)                                                                         |

### 6.2. Max length mặc định

| Loại trường | Max length             | Ghi chú                                            |
| :------------- | :--------------------- | :-------------------------------------------------- |
| Textbox        | **255 ký tự**  | Ưu tiên quy định riêng của UC nếu có        |
| Textarea       | **3000 ký tự** | Ưu tiên quy định riêng của UC nếu có        |
| Search box     | **255 ký tự**  | Tới 255 thì**block** không cho nhập thêm |

### 6.3. Placeholder

| Loại trường       | Placeholder                                                                            |
| :------------------- | :------------------------------------------------------------------------------------- |
| Text / Numeric field | *"Nhập [tên trường]"* (VD: *"Nhập số công văn"*, *"Nhập địa chỉ"*)   |
| Search box           | *"Tìm kiếm nhanh theo [tham số]"* (VD: *"Tìm kiếm nhanh theo mã báo cáo"*) |

### 6.4. Trường bắt buộc & Error Messages

| Tiêu chí                                               | Quy tắc                                                    | Error Message                                                         |
| :------------------------------------------------------- | :---------------------------------------------------------- | :-------------------------------------------------------------------- |
| Trường bắt buộc bị bỏ trống / chỉ khoảng trắng | Lỗi inline màu đỏ, tự biến mất khi nhập hợp lệ    | *"Vui lòng nhập [tên trường]"*                                 |
| Vượt max length — Search box                          | **Block** không cho nhập thêm khi đạt giới hạn | —                                                                    |
| Vượt max length — Textbox / Textarea                  | Báo lỗi inline màu đỏ khi out-click hoặc submit       | *"[Tên trường] không được vượt quá [maxlength] ký tự!"* |
| Chưa đủ min length                                    | Báo lỗi inline khi submit hoặc out-click                 | *"[Tên trường] nhập chưa đủ [minlength] ký tự!"*           |

### 6.5. Live Search

| Tiêu chí     | Quy tắc                                                                                                                                                                         |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instant Search | Lọc và hiển thị kết quả ngay khi gõ từng ký tự (real-time, partial match, case-insensitive). Không cần nhấn Enter. Áp dụng cho Search box và Searchable Dropdown |

---

## CMR_07: Quy tắc Dropdown

Áp dụng cho toàn bộ Dropdown/Combobox:

### 7.1. Single Choice Dropdown (Chọn 1 giá trị)

| Tiêu chí                      | Quy tắc                                                                                   | Error Message                         |
| :------------------------------ | :----------------------------------------------------------------------------------------- | :------------------------------------ |
| Mở danh sách                  | Nhấp vào Dropdown hiển thị toàn bộ tùy chọn                                        | —                                    |
| Tên dài                       | Vượt quá giới hạn ký tự thì cắt ngắn hiển thị "...". Hover để xem đầy đủ | —                                    |
| Chọn tùy chọn                | Nhấp chọn thì thay placeholder bằng tên đã chọn và đóng danh sách              | —                                    |
| Tô sáng                       | Khi mở lại, tùy chọn đang chọn được highlighted                                   | —                                    |
| Placeholder mặc định         | *"Chọn [tên trường]"* (VD: *"Chọn trạng thái"*, *"Chọn năm"*)               | —                                    |
| Trường bắt buộc chưa chọn | Hiển thị lỗi inline màu đỏ, tự biến mất khi chọn hợp lệ                        | *"Vui lòng chọn [tên trường]"* |

### 7.2. Multiple Choice Dropdown (Chọn nhiều giá trị)

| Tiêu chí                           | Quy tắc                                                                                                                                                         |
| :----------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A. Thành phần giao diện** |                                                                                                                                                                  |
| Input Box                            | Ô nhập liệu chính, bo góc và viền theo theme hệ thống                                                                                                   |
| Tags                                 | Giá trị đã chọn hiển thị dạng tag trong ô input, mỗi tag có dấu "✕" để xóa nhanh                                                                 |
| Counter Tag (+N...)                  | Khi tag tràn chiều ngang ô input, gom mục tràn vào tag đếm (VD:`+1...`, `+2...`). Nếu 1 tag đầu cũng không vừa thì hiển thị luôn `+1...` |
| Dropdown Menu                        | Danh sách lựa chọn hiển thị khi click vào input                                                                                                            |
| Option quá dài                     | Nếu tên tùy chọn dài vượt chiều ngang dropdown, cắt ngắn hiển thị "..." ở cuối. Hover để xem đầy đủ                                          |
| **B. Quy tắc lựa chọn**     |                                                                                                                                                                  |
| Multi-selection                      | Người dùng có thể chọn một hoặc nhiều option cùng lúc                                                                                                 |
| Đánh dấu đã chọn               | Các mục đang chọn có checkmark/highlight để phân biệt                                                                                                   |
| Hủy chọn                           | 2 cách: (1) Click mục đã chọn trong dropdown; (2) Click dấu "✕" trên Tag trong ô input                                                                  |
| **C. Quy tắc hiển thị**     |                                                                                                                                                                  |
| Thứ tự Tag                         | Các mục chọn trước hiển thị tag trước                                                                                                                   |
| Overflow (rút gọn)                 | Nếu tổng chiều rộng tag vượt chiều ngang ô input, chỉ hiển thị tag đầu tiên vừa đủ, gom còn lại vào counter tag                              |
| Tag reflow (xóa tag)                | Xóa tag thì các tag sau tự dồn lên. Nếu đủ chỗ thì hiển thị thêm tag từ counter, giảm số counter tương ứng                                   |
| Clear All                            | Xóa hết tag thì ô input hiển thị lại placeholder mặc định                                                                                              |
| **D. Quy tắc tìm kiếm**     |                                                                                                                                                                  |
| Instant Search                       | Gõ ký tự vào ô input thì dropdown tự lọc giá trị khớp (case-insensitive, partial match). Tham chiếu: CMR_06                                          |
| Không tìm thấy                    | Hiển thị text*"Không tìm thấy kết quả"* trong vùng dropdown                                                                                            |
| **E. Cuộn**                   | Danh sách**nhiều hơn 5 mục** thì tích hợp thanh cuộn dọc trong menu                                                                               |
| **F. Trường bắt buộc**     | Chưa chọn thì hiển thị lỗi inline:*"Vui lòng chọn [tên trường]"*. Tự biến mất khi chọn hợp lệ                                                 |
| **G. Kết quả lọc**          | Chọn/bỏ chọn giá trị lọc thì kết quả hiển thị ngay (real-time filter)                                                                                 |

### 7.3. Searchable Dropdown (Dropdown có ô tìm kiếm)

| Tiêu chí                                                             | Quy tắc                                                                                          | Error Message                                    |
| :--------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ | :----------------------------------------------- |
| Tìm kiếm tức thời                                                  | Gõ ký tự thì lọc danh sách real-time (case-insensitive, partial match). Tham chiếu: CMR_06 | —                                               |
| Không tìm thấy kết quả                                            | Hiển thị text*"Không tìm thấy kết quả"* trong dropdown                                   | —                                               |
| Xóa hết keyword                                                      | Dropdown hiển thị lại**placeholder** mặc định                                         | —                                               |
| Tap ra ngoài khi trống —**Filter dropdown**                   | Tự động chọn lại*"Tất cả"* (hiển thị toàn bộ). Tham chiếu: CMR_16                   | —                                               |
| Tap ra ngoài khi trống —**Form dropdown (bắt buộc)**        | Giữ trạng thái trống, hiển thị lại placeholder                                             | Lỗi inline*"Vui lòng chọn [tên trường]"* |
| Tap ra ngoài khi trống —**Form dropdown (không bắt buộc)** | Giữ trạng thái trống, hiển thị lại placeholder                                             | —                                               |

---

## CMR_08: Quy tắc hiển thị Kỳ hạn báo cáo

Cách hiển thị Tên Kỳ báo cáo: sẽ được lấy theo giá trị đã được chọn trong Trường "Chọn thời gian dữ liệu báo cáo" trong kỳ báo cáo, sẽ có các trường hợp sau:

| **Loại báo cáo định kỳ hàng** | **Chọn thời gian dữ liệu báo cáo (Single choice dropdown)**                                                                        | **Cách hiển thị Kỳ báo cáo**                                     |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Hàng tháng                               | Các giá trị trong dropdown sẽ thể hiện format: Tháng <tháng> năm <năm>`<br>`Ví dụ: Tháng 10 năm 2026                           | Tháng <tháng> năm <năm>`<br>`Ví dụ: Tháng 10 năm 2026              |
| Hàng quý                                 | Các giá trị trong dropdown sẽ thể hiện format: Quý <số thứ tự quý trong năm: 1,2,3,4> năm <năm>`<br>`Ví dụ: Quý 1 năm 2026 | Quý <thứ tự quý trong năm> năm <năm>`<br>`Ví dụ: Quý 1 năm 2026 |
| 6 tháng                                   | Các giá trị trong dropdown sẽ thể hiện format: Kỳ <thứ tự kỳ trong năm> năm <năm>`<br>`Ví dụ: Kỳ 1 năm 2026                 | Kỳ <thứ tự kỳ trong năm> năm <năm>`<br>`Ví dụ: Kỳ 1 năm 2026    |
| Năm                                       | Các giá trị trong dropdown sẽ thể hiện format: Năm <năm>`<br>`Ví dụ: Năm 2026                                                     | Năm <năm>`<br>`Ví dụ: Năm 2026                                        |

---

## CMR_09: Quy tắc mã báo cáo (Report Code)

Chi tiết quy tắc sinh mã tham chiếu **Appendices**.

| Tiêu chí         | Quy tắc                                                                                                    |
| :----------------- | :---------------------------------------------------------------------------------------------------------- |
| Cấu trúc mã     | `[Phân hệ]_[Mã Biểu]_[ID tự tăng]`                                                                  |
| Tiền tố `FDI`  | Đầu tư nước ngoài tại VN                                                                             |
| Tiền tố `ODI`  | Đầu tư ra nước ngoài                                                                                  |
| Tiền tố `DDI`  | Đầu tư trong nước                                                                                      |
| Tiền tố `EZ`   | Quản lý KCN, KKT                                                                                          |
| Tiền tố `PROM` | Xúc tiến đầu tư                                                                                        |
| Ví dụ            | `ODI_I15_1` (Báo cáo 6 tháng ĐTRNN Mẫu I.15); `PROM_BIV3_8` (Báo cáo xúc tiến đầu tư B.4.3) |
| Unique Key         | Mã báo cáo là duy nhất trên toàn hệ thống (Global Unique)                                          |

---

## CMR_10: Phân trang danh sách kỳ hạn

| Tiêu chí                        | Quy tắc                                                                                                                   |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| Loại phân trang                 | List có kỳ hạn: phân trang theo Kỳ. <br />List không kỳ hạn: phân trang theo Bản ghi                             |
| Mặc định                       | **10 bản ghi/trang**                                                                                                |
| Dropdown chọn số bản ghi/trang | Options: 10, 20, 50, 100. Thay đổi giá trị → grid tự reload, quay về trang 1                                        |
| Button [Trang trước]            | Disabled khi ở Trang 1                                                                                                    |
| Button [Trang sau]                | Disabled khi ở Trang cuối cùng                                                                                          |
| Hiển thị thông tin             | Text:*"Hiển thị [start]-[end] / [total] báo cáo"*. Số trang hiển thị các nút số trang, trang hiện tại active |

---

## CMR_11: Quy tắc hiển thị Tooltip / Giải thích trường thông tin

Áp dụng cho toàn bộ các màn hình nhập liệu thông tin báo cáo. Nếu biểu mẫu báo cáo gốc (report template) có yêu cầu giải thích chi tiết, hướng dẫn điền, hoặc tooltip cho một trường thông tin cụ thể:

- **Hiển thị:** Bắt buộc hiển thị một biểu tượng thông tin (Information icon - ℹ️) ngay bên cạnh tiêu đề/nhãn của trường thông tin đó trên thiết kế UI.
- **Tương tác:** Khi người dùng di chuột (hover) vào biểu tượng thông tin, hệ thống sẽ hiển thị một Tooltip chứa toàn bộ nội dung giải thích/hướng dẫn tương ứng từ biểu mẫu gốc.

---

## CMR_12: Quy tắc trạng thái trường dữ liệu từ API (API-sourced Fields)

Áp dụng cho toàn bộ trường có nguồn dữ liệu từ API (Master Data, Auto-fill):

| Tiêu chí                                         | Quy tắc                                                                                                                  | Error Message                                                                                                                        |
| :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------- |
| Trước khi gọi API                               | Chưa chọn Phạm vi dữ liệu nguồn input / Dự án: Trường giữ trạng thái**Disabled** — chờ kết quả API | —                                                                                                                                   |
| API trả về dữ liệu (không null/rỗng)         | Trường tự động điền giá trị và tiếp tục giữ trạng thái**Disabled** (khóa)                           | —                                                                                                                                   |
| API không trả về dữ liệu (null/rỗng)         | Trường chuyển sang**Enabled** — người dùng có thể nhập liệu thủ công                                   | —                                                                                                                                   |
| API thất bại (timeout, lỗi mạng, server error) | Trường chuyển sang**Enabled** — người dùng có thể nhập liệu thủ công                                   | Toast lỗi T05 — Tiêu đề:*"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau"* |

---

## CMR_13: Quy tắc nhập Số công văn

Áp dụng cho toàn bộ trường nhập liệu "Số công văn" trong hệ thống.

**Cấu trúc bắt buộc:** `[Số thứ tự]/[Ký hiệu 1]-[Ký hiệu 2]`

| Tiêu chí                    | Quy tắc                                                                         | Error Message                                                                    |
| :---------------------------- | :------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| Max length                    | **50 ký tự** (uu tiên quy định riêng của UC nếu có)               | Vượt max:*"[Tên trường] không được vượt quá [maxlength] ký tự!"* |
| Chữ số                      | `0–9`                                                                         | —                                                                               |
| Chữ cái                     | Tự động viết hoa (Auto-uppercase)                                            | —                                                                               |
| Dấu gạch chéo              | `/` — phân cách Số thứ tự và Ký hiệu                                  | —                                                                               |
| Dấu gạch nối               | `-` — phân cách các nhóm chữ tắt trong Ký hiệu                        | —                                                                               |
| Block ký tự không hợp lệ | Chặn khoảng trắng và ký tự đặc biệt ngoài `/` và `-` ngay khi gõ | —                                                                               |

**Quy tắc cấu thành:**

| # | Thành phần       | Quy tắc                                                                                 |
| - | ------------------ | ---------------------------------------------------------------------------------------- |
| 1 | Số thứ tự       | Là số Ả Rập. Nếu nhỏ hơn 10 phải có số 0 ở đầu (VD:`01`, `02`).         |
| 2 | Dấu phân cách 1 | Giữa Số thứ tự và Ký hiệu bắt buộc là dấu gạch chéo (`/`).                |
| 3 | Ký hiệu          | Bằng chữ in hoa.                                                                       |
| 4 | Dấu phân cách 2 | Giữa các nhóm chữ viết tắt trong Ký hiệu bắt buộc là dấu gạch nối (`-`). |
| 5 | Khoảng trắng     | KHÔNG được có bất kỳ khoảng trắng nào trong toàn bộ chuỗi.                  |

**Ví dụ hợp lệ:** `01/QĐ-UBND`, `2401/QĐ-BGDĐT`, `4433/BYT-KCB`

| Hành vi                      | Quy tắc                                                                                                                                             |
| :---------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| Auto-uppercase                | Tự động viết hoa mọi chữ cái ngay khi người dùng gõ                                                                                       |
| Auto-correct số thứ tự     | Số thứ tự < 10 mà không có số `0` đứng trước → tự động thêm `0` khi hoàn tất nhập (VD: gõ `1/QĐ-UBND` → `01/QĐ-UBND`) |
| Block ký tự không hợp lệ | Chặn khoảng trắng và mọi ký tự đặc biệt ngoài `/` và `-` ngay khi gõ, không cho phép hiển thị lên trường                     |

**Validate:**

| Trường hợp vi phạm | Thông báo lỗi                                          |
| ---------------------- | --------------------------------------------------------- |
| Thiếu dấu `/`      | *"Số công văn chưa đúng chuẩn, thiếu dấu "/""* |
| Thiếu dấu `-`      | *"Số công văn chưa đúng chuẩn, thiếu dấu "-""* |
| Sai format tổng thể  | *"Vui lòng nhập lại thông tin"*                     |

---

## CMR_14: Quy tắc cảnh báo dữ liệu chưa lưu khi điều hướng (Dirty Form Guard)

Áp dụng cho toàn bộ các màn hình nhập liệu trong hệ thống.

### 14.1. Điều kiện kích hoạt

| Điều kiện             | Mô tả                                                                                                                                                     |
| :----------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Form dirty               | Người dùng đã thay đổi giá trị của bất kỳ field nào so với giá trị tại thời điểm load form                                              |
| Điều hướng ra ngoài | Nhấn [Hủy], chuyển tab menu sidebar, navigation bar, breadcrumb, hoặc bất kỳ phương thức nào dẫn đến rời khỏi màn hình lập/sửa báo cáo |
| Không kích hoạt       | Form**không dirty** (chưa thay đổi bất kỳ field nào) → hệ thống điều hướng bình thường, không hiển thị popup                      |

> **"Thay đổi" (dirty)** được xác định bằng cách so sánh giá trị hiện tại với giá trị tại thời điểm load form hoặc lần Lưu nháp gần nhất. Áp dụng mọi cấp độ: menu sidebar, navigation bar, breadcrumb.

### 14.2. Popup cảnh báo

| Thành phần              | Nội dung                                                                                                            |
| :------------------------ | :------------------------------------------------------------------------------------------------------------------- |
| Tiêu đề                | *"Dữ liệu chưa được lưu"*                                                                                   |
| Nội dung                 | *"Bạn có chắc chắn muốn rời khỏi trang này không?"*                                                       |
| Nút**[Hủy]**      | Đóng popup, ở lại màn hình hiện tại. Dữ liệu form giữ nguyên                                             |
| Nút**[Đồng ý]** | Đóng popup, thực hiện điều hướng (về Danh sách hoặc màn hình đã chọn). Dữ liệu chưa lưu bị hủy |

### 14.3. Quy tắc chuyển tab nội bộ

| Loại báo cáo                                                               | Hành vi                                                                                                                                                                                                           |
| :---------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Báo cáo gộp** (nhiều tab biểu mẫu, Lưu nháp toàn bộ N tabs) | Dirty Form Guard**KHÔNG kích hoạt** khi chuyển tab nội bộ. Dữ liệu giữ **in-memory** — không popup. Chỉ kích hoạt khi điều hướng **ra khỏi** màn hình. Tham chiếu: CF_01.1 |
| **Báo cáo đơn lẻ** (có nhiều tab chức năng)                    | Dữ liệu giữ**in-memory** khi chuyển tab — không popup. Dirty Form Guard chỉ kích hoạt khi điều hướng **ra khỏi** màn hình                                                              |

### 14.4. Disable nút hành động (trạng thái "Yêu cầu chỉnh sửa")

Áp dụng khi bản ghi ở trạng thái **"Yêu cầu chỉnh sửa"** — người dùng bắt buộc phải chỉnh sửa trước khi Nộp hoặc Lưu nháp.

| Màn hình          | Nút             | Trạng thái                                                                                     | Tooltip khi hover                                                                     |
| :------------------ | :--------------- | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| Danh sách (CF_09)  | [Nộp]           | **Disabled** khi chưa chỉnh sửa                                                         | *"Vui lòng chỉnh sửa báo cáo trước khi nộp lại"*                           |
| Danh sách (CF_09)  | [Nộp]           | **Enabled** sau khi: vào Chỉnh sửa + thay đổi ≥ 1 trường + Lưu nháp thành công | —                                                                                    |
| Chỉnh sửa (CF_03) | [Nộp báo cáo] | **Disabled** khi form chưa dirty                                                          | *"Vui lòng chỉnh sửa ít nhất một trường thông tin trước khi nộp"*       |
| Chỉnh sửa (CF_03) | [Lưu nháp]     | **Disabled** khi form chưa dirty                                                          | *"Vui lòng chỉnh sửa ít nhất một trường thông tin trước khi lưu nháp"* |
| Chỉnh sửa (CF_03) | Cả hai nút     | **Enabled** ngay khi thay đổi bất kỳ field nào (form dirty)                           | —                                                                                    |

> **Lưu ý:** Quy tắc này **chỉ áp dụng** cho trạng thái "Yêu cầu chỉnh sửa". Các trạng thái khác (Lưu nháp) không bị ảnh hưởng — [Nộp báo cáo] và [Lưu nháp] luôn Enabled.

---

## CMR_15: Quy tắc Thêm/Xóa hàng trong bảng nhập liệu (Dynamic Table Rows)

Áp dụng cho các bảng nhập liệu có chức năng thêm/xóa hàng động.

> **Lưu ý:** Không phải tất cả bảng đều có chức năng thêm/xóa hàng — một số bảng có số lượng hàng cố định (fixed rows). Bảng nào được phép thêm/xóa hàng sẽ được ghi rõ tại UC chi tiết tương ứng.

| Nút                    | Quy tắc                                                                                                                                                                                               |
| :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Thêm hàng]** | Hiển thị ở footer bảng (bên dưới dòng cuối cùng). Nhấn → thêm 1 dòng trống mới. Các trường API trong dòng mới → Disabled (chờ chọn). Tham chiếu: CMR_12                       |
| **[Xóa hàng]**  | Hiển thị dạng icon button trên mỗi dòng. Chỉ xuất hiện khi bảng có**từ 2 dòng trở lên** — khi chỉ còn 1 dòng thì ẩn. Nhấn → xóa dòng ngay, không cần popup xác nhận |

---

## CMR_16: Quy tắc Filter Dropdown — Mặc định "Tất cả"

Áp dụng cho tất cả **filter dropdown** trên màn hình danh sách. Không áp dụng cho dropdown trong form nhập liệu.

| Tiêu chí                | Quy tắc                                                                                                                                              |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Option "Tất cả"         | Tất cả filter dropdown**bắt buộc** có option **"Tất cả"** ở đầu danh sách                                                      |
| Giá trị mặc định     | Khi mở màn hình lần đầu, mặc định chọn**"Tất cả"** — hiển thị toàn bộ bản ghi, không lọc                                    |
| Hành vi real-time        | Kết quả lọc hiển thị ngay sau khi thay đổi giá trị filter, không cần xác nhận                                                            |
| Phân biệt Form dropdown | Chỉ áp dụng cho filter/bộ lọc danh sách. Form dropdown tuân theo CMR_07 (placeholder*"Chọn [tên trường]"*, không có option "Tất cả") |

---

## CMR_17: Quy tắc Upload File Đính kèm (Attachment Upload)

Áp dụng cho các báo cáo có phần upload file đính kèm trong màn hình lập/chỉnh sửa báo cáo.

> **Lưu ý:** Không phải tất cả báo cáo đều có phần upload file. Báo cáo nào yêu cầu upload file sẽ được ghi rõ tại UC chi tiết tương ứng.

### 17.1. Giới hạn upload

| Tiêu chí                  | Giá trị                                          |
| --------------------------- | -------------------------------------------------- |
| Số lượng file tối đa   | **10 file**                                  |
| Định dạng cho phép      | `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx` |
| Tổng dung lượng tối đa | **10 MB** (tổng tất cả file đã upload)  |

### 17.2. Cách upload

| Hình thức             | Quy tắc                                                      |
| :---------------------- | :------------------------------------------------------------ |
| Click vào vùng upload | Mở File Explorer để chọn file                             |
| Kéo thả (Drag & Drop) | Kéo file trực tiếp vào vùng upload                       |
| Upload nhiều file      | Cho phép upload nhiều file cùng lúc trong một lần chọn |

### 17.3. Validate khi upload

| Trường hợp vi phạm          | Hành vi hệ thống                                                                                                                                                                      |
| :------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| File sai định dạng           | Bỏ qua file đó, hiển thị Alert inline:*"File [tên file] không đúng định dạng. Chỉ chấp nhận PDF, DOC, DOCX, XLS, XLSX"*                                                 |
| Vượt quá 10 file             | Từ chối file thứ 11 trở đi, hiển thị Alert:*"Đã đạt giới hạn tối đa 10 file đính kèm"*                                                                               |
| Tổng dung lượng vượt 10 MB | Từ chối file gây vượt hạn mức, hiển thị Alert:*"Tổng dung lượng file đính kèm vượt quá 10 MB. Vui lòng xóa bớt file hoặc chọn file có dung lượng nhỏ hơn"* |
| Lỗi server khi upload          | Toast lỗi — Tiêu đề:*"Lỗi hệ thống"*, Nội dung: *"Không thể tải file lên. Vui lòng thử lại sau"*                                                                     |

### 17.4. Hiển thị danh sách file đã upload

| Tiêu chí                      | Quy tắc                                                                         |
| :------------------------------ | :------------------------------------------------------------------------------- |
| Thông tin file                 | Mỗi file hiển thị: Tên file, Dung lượng (KB/MB), Icon xóa (🗑️ hoặc ✕) |
| Xóa file                       | Nhấn icon xóa → xóa file khỏi danh sách ngay, không cần popup xác nhận |
| Tổng số file và dung lượng | Hiển thị thông tin tổng (VD:*"3/10 file · 2.4 MB / 10 MB"*)               |

### 17.5. Quy tắc nội dung upload (Free Upload)

| Tiêu chí         | Quy tắc                                                                                                                                                                                              |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tự do nhập liệu | Hệ thống**không ràng buộc nội dung** file phải là loại tài liệu cụ thể nào                                                                                                        |
| Hướng dẫn       | Mỗi báo cáo có chú thích hướng dẫn (tooltip ℹ️ tại vùng upload) về loại tài liệu nên đính kèm theo thông tư. Nội dung hướng dẫn quy định riêng tại UC SRS tương ứng |

### 17.6. Trạng thái vùng upload theo trạng thái bản ghi

| Màn hình                         | Trạng thái upload                                                                              |
| :--------------------------------- | :----------------------------------------------------------------------------------------------- |
| Lập (CF_01) / Chỉnh sửa (CF_03) | Vùng upload**Enabled** — người dùng có thể thêm/xóa file                          |
| Xem (CF_07)                        | Vùng upload**Disabled** (Read-only) — chỉ hiển thị danh sách file, không thêm/xóa |

---

## CMR_18: Quy tắc Tab Navigation (Web)

Áp dụng cho toàn bộ màn hình nhập liệu có form trên Web/Report:

| Thao tác          | Hành vi                                                                                |
| :----------------- | :-------------------------------------------------------------------------------------- |
| Nhấn Tab | Chuyển focus sang trường kế tiếp theo thứ tự tab index của form |
| Nhấn Tab (field cuối) | Quay vòng về **field đầu tiên** của form |
| Nhấn Shift+Tab | Chuyển focus ngược lại trường trước đó |
| Tab Order | Thứ tự Tab đi theo bố cục giao diện từ trái sang phải, từ trên xuống dưới |
| Phạm vi áp dụng | Tất cả màn hình lập/chỉnh sửa báo cáo có form nhập liệu |

---

## CMR_19: Quy tắc trường Mã (Code Fields)

Áp dụng cho các trường có tên gọi theo dạng "Mã ..." (Mã dự án, Mã NKT, Mã KCN, Mã địa chỉ). Danh sách trường được xác định tại từng UC chi tiết.

| Tiêu chí              | Quy tắc                                                                | Error Message                                                                   |
| :---------------------- | :---------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| Max length mặc định  | **50 ký tự** (uu tiên quy định riêng của UC nếu có)      | Vượt max:*"[Tên trường] không được vượt quá [maxlength] ký tự"* |
| Ký tự không hợp lệ | Khoảng trắng và ký tự có dấu (tiếng Việt)                      | *"Mã không bao gồm khoảng trắng và ký tự có dấu"*                   |
| Auto-trim               | Tự động xóa khoảng trắng đầu/cuối khi out-click hoặc gửi API | —                                                                              |

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật                                                                   | Before                                                                                                                              | After                                                                                                                                                                                                                                                                                                                    | Ghi chú                                                                         |
| ---------- | ----------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| 2026-05-03 | 1.0 → 1.1  | CMR_03 (Trạng thái)                                                             | 3 trạng thái: Lưu nháp, Đã nộp, Yêu cầu chỉnh sửa                                                                        | 4 trạng thái: Lưu nháp, Chờ duyệt, Đã tiếp nhận, YC chỉnh sửa. Thêm rule quy trình 2 bước / >2 bước                                                                                                                                                                                                    | Đổi bộ trạng thái báo cáo và khóa nút Xóa                             |
| 2026-05-04 | 1.1 → 1.2  | CMR_13 (Số công văn)                                                           | (Không có)                                                                                                                        | Thêm mới: Quy tắc nhập, Auto-uppercase, Auto-correct, Block ký tự, Validate 3 trường hợp                                                                                                                                                                                                                        | Yêu cầu mới từ BA                                                            |
| 2026-05-05 | 1.2 → 1.3  | CMR_05 (Numeric)                                                                  | Không có rule trường bắt buộc                                                                                                 | Thêm: Trường bắt buộc bị bỏ trống → hiển thị lỗi inline "Trường bắt buộc"                                                                                                                                                                                                                                | Đồng bộ với CMR_06, CMR_07                                                   |
| 2026-05-05 | 1.2 → 1.3  | CMR_07 (Dropdown)                                                                 | Không có rule trường bắt buộc                                                                                                 | Thêm: Trường bắt buộc chưa chọn → hiển thị lỗi inline "Trường bắt buộc"                                                                                                                                                                                                                                   | Đồng bộ với CMR_05, CMR_06                                                   |
| 2026-05-05 | 1.2 → 1.3  | CMR_14 (Dirty Form)                                                               | (Không có)                                                                                                                        | Thêm mới: Quy tắc popup cảnh báo dữ liệu chưa lưu khi điều hướng, áp dụng mọi cấp độ navigation                                                                                                                                                                                                       | Yêu cầu mới từ BA                                                            |
| 2026-05-07 | 1.3 → 1.4  | CMR_12 (API-sourced Fields)                                                       | 3 trường hợp: Trước khi gọi API, API trả về dữ liệu, API không trả về dữ liệu                                        | Bổ sung trường hợp thứ 4: API thất bại (timeout, lỗi mạng, server error) → Toast T05 + Trường Enabled cho nhập tay                                                                                                                                                                                          | Yêu cầu từ UC053-058 audit                                                    |
| 2026-05-08 | 1.4 → 1.5  | CMR_07.2 (Multiple Choice Dropdown)                                               | Có "Chọn tất cả", placeholder `<N>+<tên trường>`, không có search/scroll/tag reflow                                      | Viết lại hoàn toàn: Tag-based input, Counter Tag (+N...), Instant Search, Scroll bar (>5 mục), Tag reflow khi xóa, bỏ "Chọn tất cả"                                                                                                                                                                            | Yêu cầu cập nhật UI                                                          |
| 2026-05-08 | 1.4 → 1.5  | CMR_15 (Dynamic Table Rows)                                                       | (Không có)                                                                                                                        | Thêm mới: Quy tắc Thêm/Xóa hàng trong bảng nhập liệu. Thêm hàng luôn hiện, Xóa hàng chỉ hiện khi ≥ 2 dòng, xóa không cần popup. Ghi chú bảng fixed rows                                                                                                                                          | Chuẩn hóa rule đã inline trong UC011-034, UC083-088                          |
| 2026-05-08 | 1.5 → 1.6  | CMR_14 (Tab nội bộ)                                                             | Chuyển tab nội bộ đều giữ in-memory, không popup                                                                             | Phân biệt: Báo cáo gộp → popup khi dirty (vì Lưu nháp per-tab); Báo cáo đơn lẻ → giữ in-memory                                                                                                                                                                                                           | Fix mâu thuẫn với CF_01.1                                                     |
| 2026-05-12 | 1.6 → 1.7  | CMR_14 (Tab nội bộ — Báo cáo gộp)                                           | Báo cáo gộp: Dirty Form Guard**kích hoạt** khi chuyển tab nội bộ, popup khi dirty                                     | Báo cáo gộp: Dirty Form Guard**KHÔNG kích hoạt** khi chuyển tab nội bộ, dữ liệu giữ in-memory, không popup. Đồng bộ CF_01.1                                                                                                                                                                        | Align với CF_01.1 v1.9 (Lưu nháp toàn bộ N tabs, in-memory khi chuyển tab) |
| 2026-05-11 | +1          | Điều kiện hiển thị nút                                                      | `Luôn hiển thị`                                                                                                                | `Tất cả trạng thái`                                                                                                                                                                                                                                                                                                | Chuẩn hóa điều kiện (INS-07)                                                |
| 2026-05-13 | 1.7 → 1.8  | CMR_17 (Upload File Đính kèm)                                                  | (Không có)                                                                                                                        | Thêm mới: Tối đa 10 file, định dạng PDF/DOC/DOCX/XLS/XLSX, tổng ≤ 10 MB. Free upload, chú thích hướng dẫn per-báo-cáo. Disabled tại màn hình Xem.                                                                                                                                                     | Yêu cầu mới từ BA                                                            |
| 2026-05-17 | 1.9 → 2.0  | Sắp xếp lại thứ tự CMR_16, CMR_17, CMR_18                                    | CMR_17 nằm trước CMR_16 (sai thứ tự số)                                                                                       | Đúng thứ tự: CMR_15 → CMR_16 → CMR_17 → CMR_18. Nội dung không thay đổi.                                                                                                                                                                                                                                      | Chuẩn hóa cấu trúc file                                                      |
| 2026-05-15 | 1.8 → 1.9  | CMR_06 (Auto trim)                                                                | Hệ thống tự động xóa khoảng trắng đầu/cuối trước khi lưu.                                                             | Hệ thống tự động xóa khoảng trắng đầu/cuối ngầm khi gửi dữ liệu lên API. Trong lúc người dùng đang nhập liệu trên giao diện, hệ thống giữ nguyên khoảng trắng đầu/cuối để không ảnh hưởng đến trải nghiệm gõ phím.                                                         | Cập nhật UX theo yêu cầu của BA                                             |
| 2026-05-17 | 1.9 → 2.0  | CMR_05 (Numeric)                                                                  | Required message:*"Trường bắt buộc"*; Max length: 500 ký tự chung                                                           | Required message:*"Vui lòng nhập [tên trường]"*; Numeric max: **18 ký tự** (khi UC không quy định riêng); Text max: 500 ký tự; Bổ sung placeholder, message max/min length, không cắt thập phân                                                                                                | Align với chuẩn chung hệ thống (Check_CMR_Report_20260517_v2)                |
| 2026-05-17 | 1.9 → 2.0  | CMR_06 (Text/Search)                                                              | Required message:*"Trường bắt buộc"*; Không có placeholder rule                                                             | Required message:*"Vui lòng nhập [tên trường]"*; Placeholder text: *"Nhập [tên trường]"*; Placeholder search: *"Tìm kiếm nhanh theo [điều kiện]"*; Bổ sung message max/min length                                                                                                                   | Align với chuẩn chung hệ thống (Check_CMR_Report_20260517_v2)                |
| 2026-05-17 | 1.9 → 2.0  | CMR_07 (Dropdown)                                                                 | Required message:*"Trường bắt buộc"*; Không có placeholder rule                                                             | Required message:*"Vui lòng chọn [tên trường]"*; Placeholder: *"Chọn [tên trường]"*                                                                                                                                                                                                                         | Align với chuẩn chung hệ thống (Check_CMR_Report_20260517_v2)                |
| 2026-05-17 | 1.9 → 2.0  | Thêm mới CMR_16 (Filter Dropdown Default)                                       | Không có rule                                                                                                                     | Filter dropdown phải có option "Tất cả", mặc định chọn "Tất cả", hiển thị toàn bộ khi mở màn hình. Phân biệt filter dropdown vs form dropdown.                                                                                                                                                        | Bổ sung theo chuẩn chung hệ thống (Check_CMR_Report_20260517_v2)             |
| 2026-05-17 | 1.9 → 2.0  | Thêm mới CMR_18 (Tab Navigation Web)                                            | Không có rule                                                                                                                     | Nhấn Tab chuyển focus sang field kế tiếp, Shift+Tab quay lại. Áp dụng tất cả form nhập liệu Report.                                                                                                                                                                                                           | Bổ sung theo chuẩn chung hệ thống (Check_CMR_Report_20260517_v2)             |
| 2026-05-18 | 2.0 -> 2.1  | Thuật ngữ nút bấm                                                             | Export / Import                                                                                                                     | Xuất báo cáo / Nhập từ file                                                                                                                                                                                                                                                                                         | Cập nhật đồng bộ tiếng Việt                                               |
| 2026-05-18 | 2.1 -> 2.2  | CS_01 Mục 2 — YearPicker behavior (tham chiếu)                                 | YearPicker disable các năm không có data. Tham chiếu: CS_01                                                                    | YearPicker enable toàn bộ các năm; năm không có data → Empty State "Không có dữ liệu". Tham chiếu: CS_01 Mục 2 (v1.7)                                                                                                                                                                                      | Bỏ logic disable năm theo yêu cầu UX                                         |
| 2026-05-20 | 2.2 -> 2.3  | CMR_03 — Trạng thái "YC chỉnh sửa"                                           | Không có [Nộp] trong danh sách hành động                                                                                     | Thêm [Nộp] (Disabled khi chưa chỉnh sửa, Enable sau khi dirty + Lưu nháp). Tham chiếu: CF_09, CMR_14                                                                                                                                                                                                             | Đồng bộ với CF_09                                                            |
| 2026-05-20 | 2.2 -> 2.3  | CMR_14 — Disable button theo dirty state                                         | Chỉ có logic popup cảnh báo khi điều hướng                                                                                  | Thêm quy tắc Disable nút [Nộp]/[Lưu nháp] khi form chưa dirty + trạng thái "YC chỉnh sửa". Tooltip hướng dẫn. Áp dụng cả Danh sách (CF_09) và Chỉnh sửa (CF_03)                                                                                                                                     | Bổ sung logic mới cho trạng thái YC chỉnh sửa                              |
| 2026-05-19 | 2.2 → 2.3  | CMR_09 Ví dụ — Tên mã biểu                                                  | Báo cáo xúc tiến đầu tư (B.IV.3)                                                                                             | Báo cáo xúc tiến đầu tư (B.4.3)                                                                                                                                                                                                                                                                                   | Đổi tên mã biểu theo quy ước mới                                         |
| 2026-05-21 | 2.3 → 2.4  | CMR_05 (Numeric) — Hiển thị lỗi trong eForm Grid                              | (Không có)                                                                                                                        | Bổ sung bullet: Lỗi trong eForm Grid hiển thị dạng**viền đỏ** quanh ô + **tooltip** chứa message lỗi khi hover (do không gian hạn chế trong ô lưới)                                                                                                                                         | Phân biệt hiển thị lỗi Form vs eForm Grid                                   |
| 2026-05-21 | 2.3 → 2.4  | CMR_06 (Text/Search) — Hiển thị lỗi trong eForm Grid                          | (Không có)                                                                                                                        | Bổ sung bullet: Lỗi trong eForm Grid hiển thị dạng**viền đỏ** quanh ô + **tooltip** chứa message lỗi khi hover (do không gian hạn chế trong ô lưới)                                                                                                                                         | Phân biệt hiển thị lỗi Form vs eForm Grid                                   |
| 2026-05-21 | 2.3 → 2.4  | CMR_07 (Dropdown) — Hiển thị lỗi trong eForm Grid                             | (Không có)                                                                                                                        | Bổ sung bullet: Lỗi trong eForm Grid hiển thị dạng**viền đỏ** quanh ô + **tooltip** chứa message lỗi khi hover (do không gian hạn chế trong ô lưới)                                                                                                                                         | Phân biệt hiển thị lỗi Form vs eForm Grid                                   |
| 2026-05-22 | 2.4 → 2.5  | CMR_08 (Kỳ hạn báo cáo)                                                       | *(Chưa định nghĩa — Chờ BA xác nhận: tên kỳ, định dạng hiển thị, logic nhóm.)*                                    | Bổ sung đầy đủ: Cách hiển thị Tên Kỳ báo cáo theo giá trị dropdown "Chọn thời gian dữ liệu báo cáo" — 4 loại: Hàng tháng, Hàng quý, 6 tháng, Năm                                                                                                                                             | BA xác nhận nội dung                                                          |
| 2026-05-24 | 2.5 → 3.0  | CMR_05 (Numeric) — Viết lại hoàn toàn                                        | Bullet dạng cũ; max 18 ký tự; error*"nhập quá ký tự cho phép"*; *"Sai định dạng số"*                               | Format bảng 3 cột; max 15 nguyên + 5 thập phân; 5 sub-sections (5.0–5.5); Validation real-time; UX auto-format; Copy/Paste giữ nguyên + báo lỗi; Error priority; Error*"Định dạng số không hợp lệ"*; *"không được vượt quá [maxlength] ký tự"*; *"nhập chưa đủ [minlength] ký tự"* | Align theo Align_CMR_Report v7.0                                                 |
| 2026-05-24 | 2.5 → 3.0  | CMR_06 (Text/Search) — Cập nhật max length + format                            | Bullet dạng cũ; max 500 chung; auto-trim khi gửi API; error*"nhập quá ký tự cho phép"*                                    | Format bảng; Textbox max**255**; Textarea max **3000**; Search box max **255** (block); auto-trim **ngầm khi gửi API**; Error *"không được vượt quá [maxlength] ký tự"*; *"nhập chưa đủ [minlength] ký tự"*                                                                | Align theo Align_CMR_Report v7.0                                                 |
| 2026-05-24 | 2.5 → 3.0  | CMR_07 — Viết lại: thêm 7.1 bảng, 7.2 gộp sub-section, thêm 7.3 Searchable | 7.1 bullet; 7.2 có A–G bullets                                                                                                    | 7.1 bảng 3 cột; 7.2 gộp A–G thành 1 bảng;**7.3 Searchable Dropdown** mới (Filter/Form-required/Form-optional tap-out logic)                                                                                                                                                                                 | Align theo Align_CMR_Report v7.0                                                 |
| 2026-05-24 | 2.5 → 3.0  | CMR_09 — Thêm tham chiếu Appendices                                            | Bullets rời                                                                                                                        | Bảng + ghi chú tham chiếu Appendices                                                                                                                                                                                                                                                                                  | Align theo Align_CMR_Report Mục B                                               |
| 2026-05-24 | 2.5 → 3.0  | CMR_10, 12, 13, 14, 15, 16, 17, 18 — Format bảng                                | Bullets dạng cũ                                                                                                                   | Chuyển toàn bộ sang bảng 2–3 cột                                                                                                                                                                                                                                                                                   | Chuẩn hóa toàn file                                                           |
| 2026-05-24 | 2.5 → 3.0  | CMR_01, 03, 04 — Gộp bullet vào bảng                                          | Bullets + bảng rời                                                                                                                | Bảng thống nhất; CMR_01 gộp Ghi chú UI vào cột 3; CMR_03 bảng trạng thái + bảng chuyển trạng thái                                                                                                                                                                                                          | Chuẩn hóa toàn file                                                           |
| 2026-05-24 | 2.5 → 3.0  | CMR_13 — Thêm max length 50                                                     | Không có giới hạn max length                                                                                                    | Bổ sung:**Max length 50 ký tự**; Block ký tự không hợp lệ ghi rõ trong bảng                                                                                                                                                                                                                              | Align theo Align_CMR_Report Mục B                                               |
| 2026-05-24 | 2.5 → 3.0  | CMR_19 — Thêm mới trường Mã                                                 | (Không có)                                                                                                                        | Bổ sung CMR_19: Trường Mã max 50, không khoảng trắng/ký tự có dấu, auto-trim                                                                                                                                                                                                                                  | Align theo Align_CMR_Report Mục B                                               |
| 2026-05-24 | 3.0 → 3.1  | CMR_05/06/07 — Fix Markdown orphan bullet                                        | Bullet ngoài bảng tại CMR_01 dòng 20                                                                                            | Gộp vào cột Ghi chú UI trong bảng CMR_01                                                                                                                                                                                                                                                                            | Fix lỗi Markdown display                                                        |
| 2026-05-24 | 3.1 → 3.2  | CMR_05/06/07 — Fix placeholder backtick                                          | Placeholder dùng backtick bọc ngoài ngoặc kép:`` `"Nhập [tên trường]"` ``                                                  | Chuyển sang italic:*"Nhập [tên trường]"* — tránh lỗi render xuống dòng                                                                                                                                                                                                                                       | Fix lỗi Markdown display                                                        |
| 2026-05-24 | 3.2 → 3.3  | CMR_05 (5.1) — Chuẩn hóa Error Message định dạng số                        | Nhiều message khác nhau:*"Ký tự không hợp lệ. Chỉ chấp nhận..."* (dài), *"Định dạng số không hợp lệ"* (ngắn) | Gom tất cả về**1 message duy nhất**: *"Định dạng số không hợp lệ"* — áp dụng cho mọi loại vi phạm định dạng                                                                                                                                                                                  | Giảm tải developer, nhất quán UX                                             |
| 2026-05-24 | 3.3 → 3.4  | CMR_05 (5.2) — Gom rule độ dài số thập phân                                | Tách riêng rule phần nguyên (có error) và phần thập phân (block)                                                           | Gộp thành 1 dòng "Số thập phân" duy nhất (tối đa 15 nguyên, 5 thập phân, tổng 21). Vượt bất kỳ phần nào đều cùng 1 error message                                                                                                                                                                   | Chuẩn hóa hành vi UI                                                          |
| 2026-05-24 | 3.4 → 3.5  | CMR_07 (7.2) — Thêm rule Option quá dài                                       | Không có quy định cho option có text dài                                                                                      | Bổ sung: Nếu tên tùy chọn dài vượt chiều ngang dropdown, cắt ngắn hiển thị "..." ở cuối. Hover để xem đầy đủ                                                                                                                                                                                        | Xử lý hiển thị text dài                                                     |
| 2026-05-24 | 3.5 → 3.6  | CMR_12 — Fix lỗi câu chữ trạng thái Disabled                                | *"chuyển sang Disabled"* (sai logic vì mặc định đang Disabled)                                                              | Sửa thành:*"tiếp tục giữ trạng thái Disabled"*                                                                                                                                                                                                                                                                  | Fix wording theo review                                                          |
| 2026-05-24 | 3.6 → 3.7  | CMR_05/06 — Fix khoảng trắng thừa trước dấu `!`                          | *"ký tự !"* (có khoảng trắng trước `!`)                                                                                  | *"ký tự!"* (không khoảng trắng)                                                                                                                                                                                                                                                                                   | Fix Markdown theo review                                                         |
